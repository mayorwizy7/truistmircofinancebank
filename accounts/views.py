from django.shortcuts import render, redirect
from .forms import AddAccountForm, EditAccountForm, RegistrationForm, TransferForm, LocalTransferForm, IntlTransferForm, UserForm, ChangePinForm, DSPForm, LoanForm, FDRForm, UserSearchForm, YourForm, CreditCardForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .models import Account, Beneficiary, TransferHistory, Pin, CreditCard
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from decimal import Decimal
from django.utils import timezone
from datetime import timedelta
from .sms import sms
import locale
import datetime
from django.http import JsonResponse




import random
# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.db.models import Q

# Email sending 
import smtplib
from email.mime.text import MIMEText
from django.db.models import Sum

zoho_sender2 = 'no-reply@truistmircofinancebank.cc'
zoho_sender = 'no-reply@truistmircofinancebank.cc'
zoho_password = 'Truistmircofinancebank1$'
# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the current date and time without milliseconds
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


@login_required(login_url='login')
def dashboard(request):
    transactions = TransferHistory.objects.filter(
        account=request.user).order_by('-transaction_time')
    
    paginator = Paginator(transactions, 5)
    page_number = request.GET.get('page')
    transactions = paginator.get_page(page_number)
    
    
    credit_card = CreditCard.objects.filter(user=request.user).order_by("-id")
    total_card = CreditCard.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0.00

    total_bal = request.user.available_balance + request.user.ledger_balance + Decimal(total_card)
    if request.method == "POST":
        random_suffix = ''.join(random.choice('0123456789') for _ in range(16))
        card_num = "51" + random_suffix
        card_cvv = random.randint(111, 999)
        form = CreditCardForm(request.POST)
        if form.is_valid():
            current_date = timezone.now().date()
            card_type = form.cleaned_data['card_type']
            print("I am valid")
            user = request.user
            name = user.first_name +" "+ user.last_name
            number = card_num
            date = current_date + timedelta(days=365 * 4)  # Add 4 years
            card = CreditCard()
            card.name = name
            card.user = user
            card.number = number
            card.expiry = date
            card.cvv = card_cvv
            card.card_type = card_type
            card.card_status = True
            card.save()
            
            
            # Notification.objects.create(
            #     user=request.user,
            #     notification_type="Added Credit Card"
            # )
            
            
            messages.success(request, "Card Added Successfully.")
            return redirect("dashboard")
    else:
        form = CreditCardForm()

    context = {'transactions': transactions,
                'form': form,
                'credit_card': credit_card,
                'total_bal': total_bal,
               }
    return render(request, 'accounts/dashboard.html', context)



def transaction_detail(request, id):
    transaction = TransferHistory.objects.get(id=id)
    total = 0  # Initialize total with a default value
    
    
    
    if transaction.fee != "Free":
        total = transaction.amount + Decimal(transaction.fee)
    else:
        total = transaction.amount
        print(total)

    context = {
        "transaction":transaction,
        "total_amount": total

    }
    return render(request, 'accounts/transaction_detail.html', context)





def transfer_success(request, id):
    transaction = TransferHistory.objects.get(id=id)
    total = 0  # Initialize total with a default value
    
    request.session['beneficiary_form_data'] = {
        'id': transaction.id,
        'receiver': transaction.receiver,
        'transfer_type': transaction.transfer_type,
        'receiver_name': transaction.receiver_name,
        'receiver_bank_name': transaction.receiver_bank_name,
        'receiver_bank_address': transaction.receiver_bank_address,
        'receiver_bank_country': transaction.receiver_bank_country,
        'receiver_IBAN': transaction.receiver_IBAN,
        'receiver_routing_number': transaction.receiver_routing_number,
    }
    
    
    if transaction.fee != "Free":
        total = transaction.amount + Decimal(transaction.fee)
    else:
        total = transaction.amount
        print(total)

    context = {
        "transaction":transaction,
        "total_amount": total

    }
    return render(request, 'accounts/transfer_success.html', context)


def add_beneficiary(request):
    form_data = request.session.get('beneficiary_form_data', {})  # Get with default

    account_details = Beneficiary.objects.create(
        account=request.user,
        acc_name=form_data.get('receiver_name', ''),  # Access values with .get()
        acc_number=form_data.get('receiver', ''),  # Access values with .get()
        bank=form_data.get('receiver_bank_name', ''),
        type=form_data.get('transfer_type', ''),
        address=form_data.get('receiver_bank_address', ''),
        rout_number=form_data.get('receiver_routing_number', ''),
        swift_code=form_data.get('receiver_IBAN', ''),  # You might want to double-check this mapping
        currency=form_data.get('receiver_bank_country', ''),
        # image=image,  # Make sure 'image' is defined correctly
    )
    return redirect('beneficiaries')



@login_required(login_url='login')
def transactions(request):
    transactions = TransferHistory.objects.filter(
        account=request.user).order_by('-transaction_time')

    paginator = Paginator(transactions, 15)
    page_number = request.GET.get('page')
    transactions = paginator.get_page(page_number)
    credit_card = CreditCard.objects.filter(user=request.user).order_by("-id")
    total_card = CreditCard.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0.00

    total_bal = request.user.available_balance + request.user.ledger_balance + Decimal(total_card)
    context = {
        'transactions': transactions,
        'total_bal': total_bal,
        }
    return render(request, 'accounts/transactions.html', context)


def search_user_by_acc_number(request):
    if request.method == 'GET' and request.is_ajax():
        acc_number = request.GET.get('acc_number')
        try:
            account = Account.objects.get(acc_number=acc_number)
            return JsonResponse({'success': True, 'name': account.acc_name})
        except Account.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})




@login_required(login_url='login')
def add_account(request):
    if request.method == 'POST':
        
        form = AddAccountForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("I got here")
            acc_name = form.cleaned_data['acc_name']
            bank = form.cleaned_data['bank']
            type = form.cleaned_data['type']
            acc_number = form.cleaned_data['acc_number']
            rout_number = form.cleaned_data['rout_number']
            swift_code = form.cleaned_data['swift_code']
            address = form.cleaned_data['address']
            currency = form.cleaned_data['currency']
            image = form.cleaned_data['image']
            acount_details = Beneficiary.objects.create(
                                        account=request.user, 
                                        acc_name=acc_name, 
                                        bank=bank, 
                                        type=type, 
                                        acc_number=acc_number, 
                                        rout_number=rout_number, 
                                        swift_code=swift_code, 
                                        address=address, 
                                        currency=currency, 
                                        image=image,
                                        )
            # acount_details.save()
            messages.success(request, f'{acc_name} is added to beneficiary successfully')
            return redirect('beneficiaries')
        else:
            messages.error(request, f'The Form is not valid')
            return redirect('add_account')
    else:
        form = AddAccountForm()
        context = {
            'form': form
                }
    return render(request, 'accounts/add_account.html', context)

# Beneficiary View Function
@login_required(login_url='login')
def beneficiaries(request):
    beneficiaries = Beneficiary.objects.filter(account=request.user).order_by('acc_name')
        
    context = {
        'beneficiaries':beneficiaries,
    }
    return render(request, 'accounts/beneficiaries.html', context)

# Function for regitseration

@login_required(login_url='login')
def edit_beneficiary(request, id):
    beneficiary_to_edit = Beneficiary.objects.get(id=id)
    if request.method == 'POST':
        beneficiary = EditAccountForm(request.POST, request.FILES, instance=beneficiary_to_edit)
        if beneficiary.is_valid():
            beneficiary.save()
            messages.success(request, 'Beneficiary update successful')
            return redirect('beneficiaries')
    else:
        user_form = EditAccountForm(instance=beneficiary_to_edit)

    context = {
        'form': user_form,
        'beneficiary_to_edit': beneficiary_to_edit,
    }
    return render(request, 'accounts/edit_beneficiary.html', context)



def check_account(request):
    if request.method == 'POST':
        form = AddAccountForm(request.POST, request.FILES)
        if form.is_valid():
            # Check the type of bank
            bank_type = form.cleaned_data['type']
            if bank_type == 'OWN BANK':
                # If it's OWN_BANK, search for the receiver
                acc_number = form.cleaned_data['acc_number']
                try:
                    receiver = Account.objects.get(acc_number=acc_number)
                    return render(request, 'accounts/search_result.html', {'receiver': receiver})
                except Account.DoesNotExist:
                    receiver = None
                    return render(request, 'accounts/search_result.html', {'receiver': receiver})

            # For other bank types, save the form data
            request.session['form_data'] = request.POST
            return redirect('confirm_payment')
    else:
        form = AddAccountForm()
    return render(request, 'accounts/beneficiaries.html', {'form': form})





# Function for regitseration


def register(request):
    acc_no = random.randint(2111111111, 2999999999)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("I got here")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            country = form.cleaned_data['country']
            currency = form.cleaned_data['currency']
            acc_number = acc_no
            user = Account.object.create_user(
                acc_number=acc_number, first_name=first_name, last_name=last_name, email=email, country=country, password=password)
            user.phone = phone
            user.open_password = password
            user.currency = currency
            user.save()
            
            current_site = get_current_site(request)
            mail_subject = 'Please, Verify Your Email'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            # ==========================ZOHO MESSAGE===============================

            recipient = email

            # create message
            msg = MIMEText(message)
            msg['Subject'] = mail_subject
            msg['From'] = zoho_sender2
            msg['To'] = recipient

            # Create server object with SSL option
            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

            # Perform operation via server
            server.login(zoho_sender2, zoho_password)
            server.sendmail(zoho_sender2, [recipient], msg.as_string())
            server.quit()
            
            # ==========================ZOHO MESSAGE NOTIFY ADMIN===============================

            recipient = 'support@truistmircofinancebank.cc'
            mail_subject = "New User Registered"
            message1 = f"Client's Name: {first_name} {last_name} \n\n Client's Email: {email} \n\n Client's Location: {country}"

            # create message
            msg = MIMEText(message1)
            msg['Subject'] = mail_subject
            msg['From'] = zoho_sender2
            msg['To'] = recipient

            # Create server object with SSL option
            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

            # Perform operation via server
            server.login(zoho_sender2, zoho_password)
            server.sendmail(zoho_sender2, [recipient], msg.as_string())
            server.quit()
            print('success')
            messages.success(
                request, 'Registration initiated, Check your email for activation link')
            return redirect('/accounts/login/?command=verification&email='+email)
        else:
            messages.error(
                request, 'Check your Phone Number. Enter your phone number is in ')
            return redirect('/accounts/register/')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

api = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_6ZzUmChtL5vUnrSeqvFE3midWmSajrMvoTjmLalh'

# +++++++++++++++++++++++++++++++++++ FUNCTION FOR ACCOUNT ACTIVATION ++++++++++++++++++++++++++++++++++++++++++++++
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        pin = random.randint(1111, 9999)
        
        user_pin = Pin()
        user_pin.account = user
        user_pin.pin = pin
        user_pin.save()
        # ==========================ZOHO MESSAGE NOTIFY ADMIN===============================

        recipient = user.email
        mail_subject = "Welcome to Truist Mircofinance Bank"
        message = render_to_string('accounts/congrats_email.html', {
                'user': user,
                'pin': pin,
                
            })

        # create message
        msg = MIMEText(message)
        msg['Subject'] = mail_subject
        msg['From'] = zoho_sender2
        msg['To'] = recipient

        # Create server object with SSL option
        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

        # Perform operation via server
        server.login(zoho_sender2, zoho_password)
        server.sendmail(zoho_sender2, [recipient], msg.as_string())
        server.quit()
        messages.success(request, 'Congratulations! Your account is activated. Check your Email for login information.')
        
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


# =======================Function for login form==========================
def login(request):
    if request.method == 'POST':
        acc_number = request.POST['acc_number']
        password = request.POST['password']

        user = auth.authenticate(acc_number=acc_number, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_admin:
                    messages.success(
                        request, 'Welcome to Truist Mircofinance Bank Admin Dashboard')
                    return redirect('admin_dashboard')
            else:
                messages.success(
                        request, 'Welcome to Truist Mircofinance Bank User Dashboard')
                return redirect('dashboard')
        else:
            messages.error(
                        request, 'Invalid crendential, check and try again!')
            return redirect('login')
    else:
        form = RegistrationForm()
        context={
            "form": form
        }
    return render(request, 'accounts/login.html', context )



@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out successfully!')
    return redirect('login', )



# +++++++++++++++++++++++++++++++++++ FUNCTION TO EDIT PROFILE ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def profile(request):
    # userprofile = get_object_or_404(Account, user=request.user.pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES,
                             instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'accounts/profile.html', context)





# +++++++++++++++++++++++++++++++++++ FUNCTION TO EDIT PROFILE ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def security(request):
    # userprofile = get_object_or_404(Account, user=request.user.pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES,
                             instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'updated successfully')
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'accounts/security.html', context)



# +++++++++++++++++++++++++++++++++++ FUNCTION TO PAY ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def pay(request):
    
    return render(request, 'accounts/pay.html', )



# +++++++++++++++++++++++++++++++++++ FUNCTION TO PAY ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def search_user(request):
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            acc_number = form.cleaned_data['acc_number']
            try:
                receiver = Account.object.get(acc_number=acc_number)
                print(receiver)
            except Account.DoesNotExist:
                receiver = None
            return render(request, 'accounts/search_result.html', {'receiver': receiver})
    else:
        form = UserSearchForm()
    return render(request, 'accounts/search_user.html', {'form': form})



# +++++++++++++++++++++++++++++++++++ FUNCTION TO PAY ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def transfer_amount(request, id):
    receiver = Account.object.get(id=id)
    
    context = {'receiver': receiver}
    
    return render(request, 'accounts/transfer_amount.html', context)






def form_view(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            print(form)
            request.session['form_data'] = request.POST
            return redirect('confirm_payment')
    else:
        form = YourForm()
    return render(request, 'accounts/transfer_amount.html', {'form': form})

    

# +++++++++++++++++++++++++++++++++++ FUNCTION TO PAY ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def confirm_payment(request):
    form_data = request.session.get('form_data')
    receiver_acc = form_data['receiver']
    destination = Account.object.get(acc_number=receiver_acc)
    print(destination)
    if request.method == 'POST':
        form = YourForm(form_data)
        if form.is_valid():
            form.save()
            del request.session['form_data']  # clear session
            data = form.cleaned_data
            receiver = data['receiver']
            print(receiver)
            destination = Account.object.get(acc_number=form.receiver)
            print(form)
            context = {'destination': destination,}
            
            return redirect('confirm_payment', context)
    else:
        form = YourForm(form_data)
        
    return render(request, 'accounts/confirm_payment.html', {'form': form, 'destination': destination})

def detail_view(request, id):
    object = get_object_or_404(TransferHistory, id=id)
    data = {
        'id': object.id,
        'name': object.name,
        # ... add more fields as needed
    }
    return JsonResponse(data)
# =======================Transfer=============================
@login_required(login_url='login')
def transfer(request):
    trans_ref_code = random.randint(1000000, 2999999999)
    trans_ref_code_2 = random.randint(100, 299)
    form = TransferForm()
    if request.method == 'POST':
        try:
            if request.user.allow_transfer:
                form = TransferForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    entered_pin = data['pin']
                    acc_number = data['acc_number']
                    receiver = data['receiver']
                    amount = data['amount']
                    remark = data['remark']

                    # get the current user
                    curr_user = request.user

                    # get the receiver user details
                    print("I was here")
                    if Account.object.filter(acc_number=receiver).exists():
                        destination = Account.object.get(acc_number=receiver)
                        user_pin = request.user.pin
                        print(user_pin.pin)

                        if entered_pin == user_pin.pin:
                            # ================Implimenting the transfer========================
                            # checking is the balance is enough to transfer from
                            if curr_user.available_balance >= amount:
                                # taking the amount from sender and adding to receiver balance
                                curr_user.available_balance = curr_user.available_balance - amount
                                destination.available_balance = destination.available_balance + amount
                                destination.last_received = amount

                                

                                credit_transaction = TransferHistory()
                                credit_transaction.account = destination
                                credit_transaction.ref_code = f'TRX-{trans_ref_code}-{trans_ref_code_2}'
                                credit_transaction.sender = f'{curr_user.first_name} {curr_user.last_name} ({curr_user.acc_number})'
                                credit_transaction.receiver = f'{destination.first_name} {destination.last_name } ({destination.acc_number})'
                                credit_transaction.remark = remark
                                credit_transaction.receiver_bank_name = 'Truist Mircofinance Bank'
                                credit_transaction.transaction_type = 'Credit'
                                credit_transaction.transfer_type = 'Internal'
                                credit_transaction.amount = amount
                                credit_transaction.status = 'Success'

                                debit_transaction = TransferHistory()
                                debit_transaction.account = curr_user
                                debit_transaction.ref_code = f'TRX-{trans_ref_code}-{trans_ref_code_2}'
                                debit_transaction.sender = f'{curr_user.first_name} {curr_user.last_name} ({curr_user.acc_number})'
                                debit_transaction.receiver = f' {destination.acc_number}'
                                debit_transaction.receiver_name = f'{destination.first_name} {destination.last_name}'
                                debit_transaction.receiver_bank_name = 'Truist Mircofinance Bank'
                                debit_transaction.remark = remark
                                debit_transaction.transaction_type = 'Debit'
                                debit_transaction.transfer_type = 'Internal'
                                debit_transaction.amount = amount
                                debit_transaction.status = 'Success'
                                

                                 # Set the locale to the user's default locale
                                locale.setlocale(locale.LC_ALL, '')

                                # Format the amount as a money value
                                formatted_amount = "${:,.2f}".format(amount)
                                curr_user_bal = "${:,.2f}".format(curr_user.available_balance)
                                # ========================== DEBIT ALERT EMAIL===============================
                                recipient = curr_user.email
                                mail_subject = "TXN Alert"
                                message1 = f"Dear {curr_user.first_name},\n\n Transaction Details:\n\nDate: {formatted_datetime} \n\n TXN-Ref: TXN-{trans_ref_code}-{trans_ref_code_2} \n\n TXN Type: Debit \n\n TXN Channel: Internal \n\n Recepient: {destination.first_name} {destination.last_name} ({destination.acc_number}) \n\n Amount: {formatted_amount} \n\n Bal: {curr_user_bal} "

                                
                                # Send SMS
                                # receiver=curr_user.phone
                                # sms(receiver, message1)
                                
                                # create message
                                msg = MIMEText(message1)
                                msg['Subject'] = mail_subject
                                msg['From'] = zoho_sender2
                                msg['To'] = recipient

                                # Create server object with SSL option
                                server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

                                # Perform operation via server
                                server.login(zoho_sender2, zoho_password)
                                server.sendmail(zoho_sender2, [recipient], msg.as_string())
                                server.quit()
                                # ========================== CREDIT ALERT EMAIL===============================
                                des_user_bal = "${:,.2f}".format(destination.available_balance)

                                recipient = destination.email
                                mail_subject = "TXN Alert"
                                message1 = f"Dear {destination.first_name},\n\n Transaction Details:\n\nDate: {formatted_datetime} \n\n TXN-Ref: TXN-{trans_ref_code}-{trans_ref_code_2} \n\n TXN Type: Credit \n\n TRX Channel: Internal Transfer \n\n Sender: {curr_user.first_name} {curr_user.last_name} ({curr_user.acc_number}) \n\n Remark: {remark} \n\n Amount: {formatted_amount} \n\n Bal: {des_user_bal} "
                                
                                # Send SMS
                                # receiver=destination.phone
                                # sms(receiver, message1)
                                
                                # create message
                                msg = MIMEText(message1)
                                msg['Subject'] = mail_subject
                                msg['From'] = zoho_sender2
                                msg['To'] = recipient

                                # Create server object with SSL option
                                server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

                                # Perform operation via server
                                server.login(zoho_sender2, zoho_password)
                                server.sendmail(zoho_sender2, [recipient], msg.as_string())
                                server.quit()
                                
                                # saving changes to both account
                                curr_user.save()
                                destination.save()
                                credit_transaction.save()
                                debit_transaction.save()
                                messages.success(request, f'You have successfully transferred ${amount} to {destination.last_name} {destination.first_name}')
                                return redirect('transfer_success', id=debit_transaction.id)
                            else:
                                messages.error(
                                    request, f'Insuficent Balance')
                                return redirect('dashboard')
                            return redirect('dashboard')
                        else:
                            print(user_pin.pin)
                            messages.error(request, f'Incorrect Pin. Try again.')
                            return redirect('dashboard')
                    else:
                        messages.error(
                                    request, f'Destination Account does not exit.')
                        return redirect('dashboard')
                else:
                    messages.error(request, f'Invalid Details, Check and try again. ensure your pin is numeric')
                    return redirect('dashboard')
            else:
                messages.error(request, f'This account is FROZEN! Kindly contact support@truistmircofinancebank.cc for help.')
                return redirect('dashboard')
        except Exception as e:
            print(f" this is the error message: {e}")
            messages.error(request, f'Something went wrong!')

    else:
        form = TransferForm()

    return render(request, 'accounts/pay.html')


# ======================= Local Transfer=============================
@login_required(login_url='login')
def localtransfer(request):
    trans_ref_code = random.randint(1000000, 2999999999)
    trans_ref_code_2 = random.randint(100, 299)
    form = LocalTransferForm()
    if request.method == 'POST':
        try:
            if request.user.allow_transfer:
                form = LocalTransferForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    entered_pin = data['pin']
                    acc_number = data['acc_number']
                    receiver = data['receiver']
                    bank_name = data['bank_name']
                    receiver_name = data['receiver_name']
                    routing_number = data['routing_number']
                    amount = data['amount']
                    remark = data['remark']

                    # get the current user
                    curr_user = request.user

                    # get the receiver user details
                    
                    
                    user_pin = request.user.pin
                    print(user_pin.pin)

                    if entered_pin == user_pin.pin:
                        print("I pin correct")
                        # ================Implimenting the transfer========================
                        # checking is the balance is enough to transfer from
                        if curr_user.available_balance >= amount:
                            # taking the amount from sender and adding to receiver balance
                            curr_user.available_balance = Decimal(curr_user.available_balance) - Decimal(amount)
                            

                            # saving changes to both account
                            curr_user.save()
                            
                            messages.success(request, f'You have successfully transferred ${amount} to {receiver_name}')

                            debit_transaction = TransferHistory()
                            debit_transaction.account = curr_user
                            debit_transaction.ref_code = f'TRX-{trans_ref_code}-{trans_ref_code_2}'
                            debit_transaction.sender = f'{curr_user.first_name} {curr_user.last_name} ({curr_user.acc_number})'
                            debit_transaction.receiver = f'{receiver_name} ({receiver})'
                            debit_transaction.receiver_bank_name = f'{bank_name}'
                            debit_transaction.receiver_routing_number = f'{routing_number}'
                            debit_transaction.remark = remark
                            debit_transaction.transaction_type = 'Debit'
                            debit_transaction.transfer_type = 'Local'
                            debit_transaction.amount = amount
                            debit_transaction.status = 'Success'
                            debit_transaction.save()
                            # ========================== DEBIT ALERT EMAIL===============================
                            # Format the amount as a money value
                            formatted_amount = "${:,.2f}".format(amount)
                            curr_user_bal = "${:,.2f}".format(curr_user.available_balance)
                            recipient = curr_user.email
                            mail_subject = "TRX Alert"
                            message1 = f"Dear {curr_user.first_name},\n\n Transaction Details:\n\nDate: {formatted_datetime}\n\nTRX-Ref: TRX-{trans_ref_code}-{trans_ref_code_2}\n\nTRX Type: Debit \n\nTRX Channel: Local Tranfer \n\n Recepient: {receiver_name} ({receiver}) \n\n Amount: {formatted_amount} \n\n Bal: {curr_user_bal}"

                            # create message
                            msg = MIMEText(message1)
                            msg['Subject'] = mail_subject
                            msg['From'] = zoho_sender2
                            msg['To'] = recipient

                            # Create server object with SSL option
                            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

                            # Perform operation via server
                            server.login(zoho_sender2, zoho_password)
                            server.sendmail(zoho_sender2, [recipient], msg.as_string())
                            server.quit()
                        else:
                            messages.error(
                                request, f'Insuficent Balance')
                            return redirect('dashboard')
                        return redirect('transfer_success', id=debit_transaction.id)
                    else:
                        print(user_pin.pin)
                        messages.error(
                                request, f'Incorrect Pin. Try again.')
                        return redirect('localtransfer')
                    
                else:
                    messages.error(request, f'Invalid Details, Check and try again. ensure your pin is numeric')
                    return redirect('localtransfer')
            else:
                messages.error(request, f'This account is FROZEN! Kindly contact support@truistmircofinancebank.cc for help.')
                return redirect('localtransfer')
        except Exception as e:
            print(e)
            messages.error(request, f'Something went wrong!')

    else:
        form = TransferForm()

    return render(request, 'accounts/local_transfer.html')


# ======================= Int'l Transfer=============================
@login_required(login_url='login')
def intltransfer(request):
    trans_ref_code = random.randint(1000000, 2999999999)
    trans_ref_code_2 = random.randint(100, 299)
    form = IntlTransferForm()
    if request.method == 'POST':
        try:
            if request.user.allow_transfer:
                form = IntlTransferForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    entered_pin = data['pin']
                    acc_number = data['acc_number']
                    receiver = data['receiver']
                    receiver_name = data['receiver_name']
                    bank_name = data['bank_name']
                    bank_address = data['bank_address']
                    bank_country = data['bank_country']
                    # routing_number = data['routing_number']
                    iban = data['iban']
                    swift_code = data['swift_code']
                    amount = data['amount']
                    remark = data['remark']

                    # get the current user
                    curr_user = request.user

                    # get the receiver user details
                    
                    
                    
                    user_pin = request.user.pin
                    print(user_pin.pin)

                    if entered_pin == user_pin.pin:
                        # ================Implimenting the transfer========================
                        # checking is the balance is enough to transfer from
                        if curr_user.available_balance >= amount:
                            # taking the amount from sender and adding to receiver balance
                            curr_user.available_balance = Decimal(curr_user.available_balance) - Decimal(amount)
                            print("I was here in Int'l TF")
                            

                            # saving changes to both account
                            curr_user.save()
                            
                            messages.success(request, f'You have initiated a transferred ${amount} to {receiver_name}')

                            debit_transaction = TransferHistory()
                            debit_transaction.account = curr_user
                            debit_transaction.ref_code = f'TRX-{trans_ref_code}-{trans_ref_code_2}'
                            debit_transaction.sender = f'{curr_user.first_name} {curr_user.last_name} ({curr_user.acc_number})'
                            debit_transaction.receiver = f'{receiver_name} ({receiver})'
                            debit_transaction.receiver_bank_name = f'{bank_name}'
                            debit_transaction.receiver_bank_address = f'{bank_address}'
                            debit_transaction.receiver_bank_country = f'{bank_country}'
                            # debit_transaction.receiver_routing_number = f'{routing_number}'
                            debit_transaction.receiver_IBAN = f'{iban}'
                            debit_transaction.remark = remark
                            debit_transaction.transaction_type = 'Debit'
                            debit_transaction.transfer_type = "Int'l"
                            debit_transaction.amount = amount
                            debit_transaction.status = 'Pending'
                            debit_transaction.fee = 'Free'
                            debit_transaction.save()
                        # ========================== DEBIT ALERT EMAIL===============================
                            recipient = curr_user.email
                            mail_subject = "TRX Alert"
                            message1 = f"Dear Customer,\n\n Transaction Details:\n\n TRX type: Debit \n\n TRX Channel: Int'l Transfer \n\n Recepient: {receiver_name} ({receiver}) \n\n Amount: {amount} \n\n TRX-Ref: TRX-{trans_ref_code}-{trans_ref_code_2}"

                            # create message
                            msg = MIMEText(message1)
                            msg['Subject'] = mail_subject
                            msg['From'] = zoho_sender2
                            msg['To'] = recipient

                            # Create server object with SSL option
                            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

                            # Perform operation via server
                            server.login(zoho_sender2, zoho_password)
                            server.sendmail(zoho_sender2, [recipient], msg.as_string())
                            server.quit()
                        else:
                            messages.error(
                                request, f'Insuficent Balance')
                            return redirect('dashboard')
                        return redirect('dashboard')
                    else:
                        print(user_pin.pin)
                        messages.error(
                                request, f'Incorrect Pin. Try again.')
                        return redirect('intltransfer')
                    
                else:
                    messages.error(request, f'Invalid Details, Check and try again. ensure your pin is numeric')
                    return redirect('intltransfer')
            else:
                messages.error(request, f'This account is FROZEN! Kindly contact support@truistmircofinancebank.cc for help.')
                return redirect('intltransfer')
        except Exception as e:
            print(e)
            messages.error(request, f'Something went wrong!')

    else:
        form = TransferForm()

    return render(request, 'accounts/intl_transfer.html')

# +++++++++++++++++++++++++++++++++++ INTERNATIONAL TRANSFER FORM ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def transfer_form(request):
    if request.method == 'POST':
        form = IntlTransferForm(request.POST)
        if form.is_valid():
            # Form is valid, proceed with further processing
            form_data = form.cleaned_data
            entered_pin = form_data['pin']
            user_pin = request.user.pin
            if entered_pin == user_pin.pin:
                request.session['transfer_form_data'] = form_data
                request.session['otp'] = generate_otp(request)
                print("OTP Generated. Redirecting to OTP verification page.")
                return redirect('otp_verification')
            else:
                messages.error(request, 'Incorrect PIN. Please try again.')
                return redirect('intltransfer')
        else:
            print("Form errors:", form.errors)  # Print form errors for debugging
            messages.error(request, 'Invalid form data. Please check the form fields.')
            return redirect('intltransfer')
    else:
        form = IntlTransferForm()
    
    return render(request, 'accounts/intl_transfer.html', {'form': form})



# +++++++++++++++++++++++++++++++++++ LOCAL TRANSFER FORM ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def local_transfer_form(request):
    if request.method == 'POST':
        form = LocalTransferForm(request.POST)
        if form.is_valid():
            
            #getting the form data and storing it in a variable called form_data
            form_data = form.cleaned_data
            
            #gettting the entered pin for validation
            entered_pin = form_data['pin']

            #getting the user pin from database for comparism
            user_pin = request.user.pin
            
            #Pin validation
            if entered_pin == user_pin.pin:
                
                
                #saving the form data in session temporily to pass to the validating 
                request.session['transfer_form_data'] = form_data

                # Generate OTP and also save it in session 
                request.session['otp'] = generate_otp(request)

            # Redirect to OTP verification page
                return redirect('local_otp_verification')
            else:
                messages.error(
                        request, f'Incorrect Pin. Try again.')
                return redirect('local_transfer')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = IntlTransferForm()
    
    return render(request, 'accounts/local_transfer.html', {'form': form})


# +++++++++++++++++++++++++++++++++++ LOCAL TRANSFER VALIDATION ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def local_otp_verification(request):
    trans_ref_code = random.randint(1000000, 2999999999)
    trans_ref_code_2 = random.randint(100, 299)
    
    if 'transfer_form_data' not in request.session or 'otp' not in request.session:
        # Handle the case where the session data is missing
        
        messages.error(request, f'Session Expired. Enter details to continue.')
        return redirect('local_transfer')
        # return redirect('transfer_form')

    if request.method == 'POST':
        otp = request.POST.get('otp')
        stored_otp = request.session['otp']

        if otp == stored_otp:
            form_data = request.session['transfer_form_data']
            print(form_data)
            print(otp)

            try:
                if request.user.allow_transfer:
                    form = LocalTransferForm(form_data)
                    # form = IntlTransferForm(request.POST)
                    if form.is_valid():
                        data = form.cleaned_data
                        entered_pin = data['pin']
                        acc_number = data['acc_number']
                        receiver = data['receiver']
                        receiver_name = data['receiver_name']
                        bank_name = data['bank_name']
                        routing_number = data['routing_number']
                        amount = Decimal(data['amount'])
                        remark = data['remark']
                        # form_data['transfer_amount'] = Decimal(form_data['transfer_amount'])

                        # get the current user
                        curr_user = request.user

                        # get the receiver user details
                        # ================Implimenting the transfer========================
                        # checking is the balance is enough to transfer from
                        if curr_user.available_balance >= amount:
                            # taking the amount from sender and adding to receiver balance
                            
                            percentage = Decimal(0.5)
                            charges = amount * (percentage / 100)
                            curr_user.available_balance = curr_user.available_balance - amount
                            curr_user.available_balance = curr_user.available_balance - charges
                            curr_user.ledger_balance = curr_user.ledger_balance + amount
                            print(f"this is the fee of {charges}")
                            

                            print("Iam about to save transaction") 
                            # saving changes to both account
                            curr_user.save()
                            
                            messages.success(request, f'You have initiated a local transfer of ${amount} to {receiver_name}')

                            debit_transaction = TransferHistory()
                            debit_transaction.account = curr_user
                            debit_transaction.ref_code = f'TRX-{trans_ref_code}-{trans_ref_code_2}'
                            debit_transaction.sender = f'{curr_user.first_name} {curr_user.last_name} ({curr_user.acc_number})'
                            debit_transaction.receiver = f'{receiver}'
                            debit_transaction.receiver_name = f'{receiver_name}'
                            debit_transaction.receiver_bank_name = f'{bank_name}'
                            debit_transaction.receiver_routing_number = f'{routing_number}'
                            debit_transaction.remark = remark
                            debit_transaction.transaction_type = 'Debit'
                            debit_transaction.transfer_type = "Local"
                            debit_transaction.amount = amount
                            debit_transaction.status = 'Pending'
                            debit_transaction.fee = str(charges)
                            debit_transaction.save()
                        # ========================== DEBIT ALERT EMAIL===============================
                            # Format the amount as a money value
                            formatted_amount = "${:,.2f}".format(amount)
                            curr_user_bal = "${:,.2f}".format(curr_user.available_balance)
                            recipient = curr_user.email
                            mail_subject = "TRX Alert"
                            message1 = f"Dear {curr_user.first_name},\n\n Transaction Details:\n\nDate: {formatted_datetime}\n\nTRX-Ref: TRX-{trans_ref_code}-{trans_ref_code_2}\n\nTRX Type: Debit \n\nTRX Channel: Local Tranfer \n\n Recepient: {receiver_name} ({receiver}) \n\n Amount: {formatted_amount} \n\n Bal: {curr_user_bal}"
                            
                            
                            # Send SMS 
                            receiver=curr_user.phone
                            # sms(receiver, message1)
                            # create message
                            msg = MIMEText(message1)
                            msg['Subject'] = mail_subject
                            msg['From'] = zoho_sender2
                            msg['To'] = recipient

                            # Create server object with SSL option
                            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

                            # Perform operation via server
                            server.login(zoho_sender2, zoho_password)
                            server.sendmail(zoho_sender2, [recipient], msg.as_string())
                            server.quit()
                        else:
                            messages.error(
                                request, f'Insuficent Balance')
                            return redirect('dashboard')
                        return redirect('transfer_success', id=debit_transaction.id)
                    else:
                        messages.error(request, f'Invalid Details, Check and try again. ensure your pin is numeric')
                        return redirect('local_transfer')
                else:
                    messages.error(request, f'This account is FROZEN! Kindly contact support@truistmircofinancebank.cc for help.')
                    return redirect('local_transfer')
            except Exception as e:
                print(e)
                messages.error(request, f'Something went wrong!')
        else:
            messages.error(request, 'Invalid OTP, Try again')
            return redirect('local_otp_verification')
    
    return render(request, 'accounts/local_otp_verification.html')






# +++++++++++++++++++++++++++++++++++ OTP GENERATION ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def generate_otp(request):
    # Generate a 6-digit OTP
    otp = random.randint(100000, 999999)

        
    recipient = request.user.email
    receiver = request.user.phone
    print(receiver)
    customer = request.user
    mail_subject = "OTP"
    # name = request.user
    message1 = f"Dear {customer},\n\nYou have initiated a transaction and you are required to provide a one time password (OTP) to proceed. \n\n The OTP for the transaction is {otp}\n\n NOTE: OTP Expires in 10 minutes!"

    # sms(receiver, message1)

    print(message1)
    # create message
    msg = MIMEText(message1)
    msg['Subject'] = mail_subject
    msg['From'] = zoho_sender2
    msg['To'] = recipient

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operation via server
    server.login(zoho_sender2, zoho_password)
    server.sendmail(zoho_sender2, [recipient], msg.as_string())
    server.quit()
    return str(otp)


# +++++++++++++++++++++++++++++++++++ INTERNATIONAL TRANSFER VALIDATION ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def otp_verification(request):
    trans_ref_code = random.randint(1000000, 2999999999)
    trans_ref_code_2 = random.randint(100, 299)
    
    if 'transfer_form_data' not in request.session or 'otp' not in request.session:
        # Handle the case where the session data is missing
        
        messages.error(request, f'Session Expired. Enter details to continue.')
        return redirect('intltransfer')
        # return redirect('transfer_form')

    if request.method == 'POST':
        otp = request.POST.get('otp')
        stored_otp = request.session['otp']

        if otp == stored_otp:
            form_data = request.session['transfer_form_data']
            print(form_data)

            try:
                if request.user.allow_transfer:
                    form = IntlTransferForm(form_data)
                    print("Before Validation")
                    if form.is_valid():
                        data = form.cleaned_data
                        entered_pin = data['pin']
                        acc_number = data['acc_number']
                        receiver = data['receiver']
                        receiver_name = data['receiver_name']
                        bank_name = data['bank_name']
                        bank_address = data['bank_address']
                        bank_country = data['bank_country']
                        iban = data['iban']
                        amount = Decimal(data['amount'])
                        remark = data['remark']
                        # form_data['transfer_amount'] = Decimal(form_data['transfer_amount'])

                        # get the current user
                        curr_user = request.user

                        # get the receiver user details
                        # ================Implimenting the transfer========================
                        # checking is the balance is enough to transfer from
                        if curr_user.available_balance >= amount:
                            # taking the amount from sender and adding to receiver balance
                            
                            percentage = Decimal(0.5)
                            charges = amount * (percentage / 100)
                            curr_user.available_balance = curr_user.available_balance - amount
                            curr_user.available_balance = curr_user.available_balance - charges
                            curr_user.ledger_balance = curr_user.ledger_balance + amount
                            print(f"this is the fee of {charges}")
                            

                            print("Iam about to save transaction") 
                            # saving changes to both account
                            curr_user.save()
                            
                            messages.success(request, f'You have initiated a transferred of ${amount} to {receiver_name}')

                            debit_transaction = TransferHistory()
                            debit_transaction.account = curr_user
                            debit_transaction.ref_code = f'TRX-{trans_ref_code}-{trans_ref_code_2}'
                            debit_transaction.sender = f'{curr_user.first_name} {curr_user.last_name} ({curr_user.acc_number})'
                            debit_transaction.receiver = f'{receiver}'
                            debit_transaction.receiver_name = f'{receiver_name}'
                            debit_transaction.receiver_bank_name = f'{bank_name}'
                            debit_transaction.receiver_bank_address = f'{bank_address}'
                            debit_transaction.receiver_bank_country = f'{bank_country}'
                            debit_transaction.receiver_IBAN = f'{iban}'
                            debit_transaction.remark = remark
                            debit_transaction.transaction_type = 'Debit'
                            debit_transaction.transfer_type = "Int'l"
                            debit_transaction.amount = amount
                            debit_transaction.status = 'Pending'
                            debit_transaction.fee = str(charges)
                            debit_transaction.save()
                        # ========================== DEBIT ALERT EMAIL===============================
                             # Format the amount as a money value
                            formatted_amount = "${:,.2f}".format(amount)
                            curr_user_bal = "${:,.2f}".format(curr_user.available_balance)
                            recipient = curr_user.email
                            mail_subject = "TRX Alert"
                            message1 = f"Dear {curr_user.first_name},\n\nTransaction Details:\n\nDate: {formatted_datetime}\n\nTRX-Ref: TRX-{trans_ref_code}-{trans_ref_code_2}\n\nTRX Type: Debit \n\nTRX Channel: Int'l Tranfer \n\n Recepient: {receiver_name} ({receiver}) \n\n Amount: {formatted_amount} \n\n Bal: {curr_user_bal}"

                            
                            # Send SMS
                            receiver=curr_user.phone
                            # sms(receiver, message1)
                            
                            # create message
                            msg = MIMEText(message1)
                            msg['Subject'] = mail_subject
                            msg['From'] = zoho_sender2
                            msg['To'] = recipient

                            # Create server object with SSL option
                            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

                            # Perform operation via server
                            server.login(zoho_sender2, zoho_password)
                            server.sendmail(zoho_sender2, [recipient], msg.as_string())
                            server.quit()
                        else:
                            messages.error(
                                request, f'Insuficent Balance')
                            return redirect('dashboard')
                        return redirect('transfer_success', id=debit_transaction.id)
                    else:
                        messages.error(request, f'Invalid Details, Check and try again. ensure your pin is numeric')
                        return redirect('intltransfer')
                else:
                    messages.error(request, f'This account is FROZEN! Kindly contact support@truistmircofinancebank.cc for help.')
                    return redirect('intltransfer')
            except Exception as e:
                print(e)
                messages.error(request, f'Something went wrong!')
        else:
            messages.error(request, 'Invalid OTP, Try again')
            return redirect('otp_verification')
    
    return render(request, 'accounts/otp_verification.html')


# +++++++++++++++++++++++++++++++++++ FUNCTION FOR FORGOT PASSWORD ++++++++++++++++++++++++++++++++++++++++++++++
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.object.filter(email=email).exists():
            user = Account.object.get(email__exact=email)

            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            recipient = email

            # create message
            msg = MIMEText(message)
            msg['Subject'] = mail_subject
            msg['From'] = zoho_sender
            msg['To'] = recipient

            # Create server object with SSL option
            server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

            # Perform operation via server
            server.login(zoho_sender, zoho_password)
            server.sendmail(zoho_sender, [recipient], msg.as_string())
            server.quit()

            messages.success(
                request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')

# +++++++++++++++++++++++++++++++++++ FUNCTION FOR PASSWORD RESET VALIDATION ++++++++++++++++++++++++++++++++++++++++++++++


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link is expired!')
        return redirect('login')

# +++++++++++++++++++++++++++++++++++ FUNCTION TO RESET PASSWORD ++++++++++++++++++++++++++++++++++++++++++++++


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.object.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')


# +++++++++++++++++++++++++++++++++++ FUNCTION TO CHANGE PASSWORD ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.object.get(acc_number__exact=request.user.acc_number)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()

                auth.logout(request)
                messages.success(
                    request, 'Your password has been updated successfully')
                return redirect('login')
            else:
                messages.error(request, 'Invalid current password')
                return redirect('security')
        else:
            messages.error(request, 'Your new password does not match')
            return redirect('security')

    return render(request, 'accounts/security.html')


# +++++++++++++++++++++++++++++++++++ FUNCTION TO CHANGE PASSWORD ++++++++++++++++++++++++++++++++++++++++++++++
@login_required(login_url='login')
def change_pin(request):
    # pin_form = ChangePinForm()
    if request.method == 'POST':
        pin_form = ChangePinForm(request.POST)
        if pin_form.is_valid():
            current_pin = pin_form.cleaned_data['current_pin']
            new_pin = pin_form.cleaned_data['new_pin']
            confirm_pin = pin_form.cleaned_data['confirm_pin']

            user_pin = request.user.pin

            if current_pin == user_pin.pin:
                if new_pin == confirm_pin:
                    user_pin.pin = new_pin
                    user_pin.save()
                    messages.success(
                        request, 'Your PIN has been updated successfully')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Your new PIN does not match')
                    return redirect('change_password')
            else:
                messages.error(request, 'Invalid current PIN')
                return redirect('change_pin')
    else:
        pin_form = ChangePinForm()
        

    return render(request, 'accounts/change_pin.html')

def E_500(request):
    return render(request, '500.html')


def E_404(request, exception=None):
    return render(request, '404.html')