from decimal import Decimal
from django.shortcuts import render
# from accounts.forms import KycActivationForm
from accounts.models import Account, TransferHistory, Pin, Contact
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
import datetime
from .forms import CreditorForm, CountdownForm, TransactionsForm, UpdateHistoryForm, RegistrationForm, UserForm
from random import randint, random
from django.contrib import messages, auth
from django.contrib.admin.views.decorators import user_passes_test
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from django.utils import timezone
from datetime import timedelta

import smtplib
from email.mime.text import MIMEText
from django.http import HttpResponseServerError, JsonResponse

sender = 'no-reply@wealthwave.cc'
sender_password = 'Wealthwave1$'

import random
# Create your views here.


def is_admin(user):
    return user.is_admin


@login_required(login_url='login')
@user_passes_test(is_admin)
def client_list(request):
    clients = Account.object.all()
    form = RegistrationForm()
    context ={
        'clients': clients,
        'reg_form': form,
        }
    return render(request, 'backend/client_list.html', context)



@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_dashboard(request):
    clients = Account.object.all()
    total_users = Account.object.count()
    transactions = TransferHistory.objects.all()
    form = RegistrationForm()

    context = {
        'transactions': transactions,
        'clients': clients, 
        'total_users': total_users,
        'reg_form': form,
    }
    return render(request, 'backend/dashboard.html', context)



from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='login')
@user_passes_test(is_admin)
def user_profile(request, id):
    form = CountdownForm()
    trans_form = TransactionsForm()
    
    try:
        # Retrieve the Account instance for the given id
        client = get_object_or_404(Account, id=id)
        
        try:
            # Attempt to retrieve the Pin object associated with the client's account
            pin = Pin.objects.get(account=client)
        except ObjectDoesNotExist:
            # If no Pin object is found, set pin to None
            pin = None
        
        # Retrieve all transactions related to the user with the given id
        transactions = TransferHistory.objects.filter(account=client).order_by('-transaction_time')
        
        context = {
            'client': client, 
            'transactions': transactions,
            'form': form,
            'trans_form': trans_form,
            'pin': pin,
        }
        
        return render(request, 'backend/user_profile.html', context)
    
    except ObjectDoesNotExist:
        # Handle the case where the Account object does not exist
        error_message = "Account matching query does not exist for the specified ID."
        return HttpResponseServerError(error_message)




@login_required(login_url='login')
@user_passes_test(is_admin)
def add_profit(request, id):
    if request.method == 'POST':
        form = CreditorForm(request.POST)
        # print(f'I got here {form}')
        if form.is_valid():
            account = get_object_or_404(Account, id=id)
            print(f"form is valid {account}")
            amount = form.cleaned_data['amount']
            profit = Decimal(amount)
            profit = round(profit, 2)
            # client.user = client
            account.profit += profit
            account.balance += profit
            # print(amount)
            account.days_to_run -= 1
            account.counter += 1
            account.save()
            btc_price = Btc.objects.get()
            value = profit/Decimal(btc_price.price)
            btc_value = round(value, 6)
            
            # SAVING TRANSACTION HISTORY
            trans_ref_code = randint(1000000, 2999999999)
            trans_ref_code_2 = randint(100, 299)
            transaction = Transactions()
            transaction.ref_code = f'TRS-{trans_ref_code}-{trans_ref_code_2}'
            transaction.account = account
            transaction.value = f"{btc_value}BTC"
            transaction.transaction_type = "Profit Credit"
            transaction.amount = profit
            transaction.status = "Completed"
            transaction.save()
            print("i am working")
            email = account.email
            balance = account.balance
            subject = transaction.transaction_type
            message = f"Dear {account.first_name}, \n\nYour wallet was credited ${profit} from your auto-trade verified trades. \n\nNew balance: {balance}"
            send_mail(email, message, subject)
            messages.success(request, f'You have added the PROFIT of ${profit} to {account.first_name} account successfully! ')
        return redirect('user_profile', id=account.id)
    return render(request, 'backend/dashboard.html')






@login_required(login_url='login')
@user_passes_test(is_admin)
def add_bonus(request, id):
    if request.method == 'POST':
        form = CreditorForm(request.POST)
        # print(f'I got here {form}')
        if form.is_valid():
            account = get_object_or_404(Account, id=id)
            print(f"form is valid {account}")
            amount = form.cleaned_data['amount']
            profit = Decimal(amount)
            profit = round(profit, 2)
            # client.user = client
            account.bonus += profit
            # print(amount)
            account.save()
            btc_price = Btc.objects.get()
            value = profit/Decimal(btc_price.price)
            btc_value = round(value, 6)
            
            # SAVING TRANSACTION HISTORY
            trans_ref_code = randint(1000000, 2999999999)
            trans_ref_code_2 = randint(100, 299)
            transaction = Transactions()
            transaction.ref_code = f'TRS-{trans_ref_code}-{trans_ref_code_2}'
            transaction.account = account
            transaction.value = f"{btc_value}BTC"
            transaction.transaction_type = 'Bonus Credit'
            transaction.amount = profit
            transaction.status = "Completed"
            transaction.save()
            print("i am working")
            email = account.email
            balance = account.bonus
            subject = transaction.transaction_type
            message = f"Dear {account.first_name}, \n\nYour bonus wallet was credited ${profit} \n\nLogin to your account to make withdraw from your bunus wallet. \n\nNew bonus balance: {balance}"
            send_mail(email, message, subject)
            messages.success(request, f'You have added the BONUS of ${profit} to {account.first_name} Bonus account successfully! ')
        return redirect('user_profile', id=account.id)
    return render(request, 'backend/dashboard.html')




@login_required(login_url='login')
@user_passes_test(is_admin)
def clear_user(request, id):
    if request.method == 'POST':
        form = CreditorForm(request.POST)
        # print(f'I got here {form}')
        account = get_object_or_404(Account, id=id)
        historys = TransferHistory.objects.filter(account=account)
        
        if form.is_valid():
            print("i got here")
            print(f"form is valid {account}")
            amount = form.cleaned_data['amount']
            
            # client.user = client
            account.available_balance = 0
            account.credit_card = 0
            account.ledger_balance = 0
            account.wallet = 0
            account.last_received = 0
            account.allow_transfer = False
            for history in historys:
                history.delete()
            # print(amount)
            account.save()
            messages.success(
                request, f'You have RESET {account.first_name} account successfully! ')
        return redirect('user_profile', id=account.id)
    return render(request, 'backend/dashboard.html')




@login_required(login_url='login')
@user_passes_test(is_admin)
def proof(request):
    proof = Payment.objects.all().order_by('-date')
    
    context = {
        'payment_proof': proof,
    }
    
    return render(request, 'backend/proof.html', context)




@login_required(login_url='login')
@user_passes_test(is_admin)
def kyc_admin(request,):
    clients = Account.objects.filter(Q(kyc=False) & Q(kyc_submitted=True))
    context ={
        'clients': clients,
        }
    
    return render(request, 'backend/kyc_admin.html', context)




@login_required(login_url='login')
@user_passes_test(is_admin)
def kyc_details(request, id):
    account = get_object_or_404(Account, id=id)
    form = KycActivationForm(instance=account)
    context ={
        'client': account,
        'kyc_form': form,
        }
    
    return render(request, 'backend/kyc_details.html', context)




@login_required(login_url='login')
@user_passes_test(is_admin)
def kyc_update(request, id):
    account = get_object_or_404(Account, id=id)
    if request.method == 'POST':
        form = KycActivationForm(request.POST)
        print(f'I got here {form}')
        if form.is_valid():
            kyc = form.cleaned_data['kyc']
            print(kyc)
            account.kyc = kyc
            account.save()
            messages.success(
                request, f"You have updated {account.first_name}'s KYC successfully! ")
        return redirect('kyc_details', id=account.id)




@login_required(login_url='login')
@user_passes_test(is_admin)
def packages(request,):
    packages = Package.objects.all().order_by('-name')
    package_form = PackageForm()
    context = {
        'packages': packages,
        'package_form': package_form,
    }
    
    return render(request, 'backend/packages.html', context)



@login_required(login_url='login')
@user_passes_test(is_admin)
def update_packages(request, id):
    package = Package.objects.get(id=id)
    if request.method == 'POST':
        form = PackageForm(request.POST, instance=package)  # Pass the instance here
        if form.is_valid():
            form.save()  # This will update the existing package with new data
            messages.success(request, f'You have updated {package.name} Package successfully!')
            return redirect('packages')  # Redirect to the update_packages view
    package_form = PackageForm()
    context = {
        'packages': package,
        'package_form': package_form,
    }
    
    return render(request, 'backend/update_packages.html', context)



@login_required(login_url='login')
@user_passes_test(is_admin)
def add_packages(request):
    
    if request.method == 'POST':
        form = PackageForm(request.POST)  # Pass the instance here
        if form.is_valid():
            name = form.cleaned_data['name']  
            amount = form.cleaned_data['amount']  
            number_of_days = form.cleaned_data['number_of_days']  
            is_active = form.cleaned_data['is_active']  
            package = Package()
            
            package.name = name
            package.amount = amount
            package.number_of_days = number_of_days
            package.is_active = is_active
            package.save()
            messages.success(request, f'You have added ${package.name} to Packages successfully! ')
            return redirect('packages')
    package_form = PackageForm()
    context = {
        'packages': packages,
        'package_form': package_form,
    }
    
    return render(request, 'backend/update_packages.html', context)


#===================================== AUO PROFIT ADDING ========================================================
@login_required(login_url='login')
@user_passes_test(is_admin)
def auto_add_profit(request):
    if request.method == 'POST':
        form = CreditorForm(request.POST)
        # print(f'I got here {form}')
        if form.is_valid():
            accounts = Account.objects.all()
            for account in accounts:
                if account.on_timer == True:
                    print(f"form is valid {account}")
                    amount = form.cleaned_data['amount']
                    profit = Decimal(account.daily_percentage)
                    increase_percentage = round(profit, 2)
                    increase_amount = account.invested * (increase_percentage / 100)
                    # client.user = client
                    account.profit += increase_amount
                    account.balance += increase_amount
                    # account.days_to_run -= 1
                    # account.counter += 1
                    account.save()
                    btc_price = Btc.objects.get()
                    value = profit/Decimal(btc_price.price)
                    btc_value = round(value, 6)
                    
                    # SAVING TRANSACTION HISTORY
                    trans_ref_code = randint(1000000, 2999999999)
                    trans_ref_code_2 = randint(100, 299)
                    transaction = Transactions()
                    transaction.ref_code = f'TRS-{trans_ref_code}-{trans_ref_code_2}'
                    transaction.account = account
                    transaction.value = f"{btc_value}BTC"
                    transaction.transaction_type = "Profit Credit"
                    transaction.amount = increase_amount
                    transaction.status = "Completed"
                    transaction.save()
                    print("i am working")
                    email = account.email
                    balance = account.balance
                    subject = transaction.transaction_type
                    # total = round(increase_amount, 2)
                    message = f"Dear {account.first_name}, \n\nYour wallet was credited ${increase_amount} from your auto-trade verified trades. \n\nNew balance: ${balance}"
                    send_mail(email, message, subject)
                    
                    referral = Referral.objects.filter(referrer=account)
                    referral_count = referral.count()
                    print(f'This is the referral count {referral_count} for {account}')
                    messages.success(request, f'You have added the PROFIT of account all active traders successfully! ')
                    # if account.counter == 7:
                    #     # if account.no_referrals >= 2:
                    #     account.available = account.balance
                    #     account.on_timer = False
                    #     print(amount)
                    #     account.save()
                    #     aval = round(account.available, 2)
                    #     email = account.email
                    #     balance = account.balance
                    #     subject = 'Trade Completed and Withdrawal Available'

                    #     message = f"Dear {account.first_name}, \n\nYour account is due for withdrawal.\n\nThe Total of ${aval} is available for your withdrawal. \n\nThis is the total sum of your investement plus the ROI for the passed 7 days"
                    #     send_mail(email, message, subject)
                    #     messages.success(
                    #         request, f'You have added ${amount} to {account.first_name} WITHDRAWABLE BALANCE successfully! ')
                        # else:
                        #     account.available = account.invested
                        #     account.on_timer = False
                        #     account.save()
                        #     email = account.email
                        #     balance = account.balance
                        #     aval = round(account.available, 2)
                        #     subject = 'Trade Completed and Withdrawal Available'
                        #     message = f"Dear {account.first_name}, \n\nYour account is due for withdrawal.\n\nThe Total of ${aval} is available for your withdrawal. \n\nThis is the total sum of your investement only as you were unable to referr the minimum requirement of 2 persons."
                        #     send_mail(email, message, subject)
                        #     messages.success(
                        #         request, f'You have added ${account.invested} to {account.first_name} WITHDRAWABLE BALANCE successfully! ')
                    
            messages.success(request, f'You have added the PROFIT of account all active traders successfully! ')

        return redirect('client_list')
    return render(request, 'backend/dashboard.html')



@login_required(login_url='login')
@user_passes_test(is_admin)
def add_transaction(request, id):
    if request.method == 'POST':
        form = TransactionsForm(request.POST)
        # print(f'I got here {form}')
        if form.is_valid():
            account = get_object_or_404(Account, id=id)
            # client = Transactions.objects.get(account=account)
            print(f"form is valid {account}")
            transaction_type = form.cleaned_data['transaction_type']
            sender = form.cleaned_data['sender']
            receiver = form.cleaned_data['receiver']
            transaction_type = form.cleaned_data['transaction_type']
            transfer_type = form.cleaned_data['transfer_type']
            amount = form.cleaned_data['amount']
            receiver_bank_name = form.cleaned_data['receiver_bank_name']
            amount = form.cleaned_data['amount']
            fee = form.cleaned_data['fee']  
            status = form.cleaned_data['status']  
            decimal_amount = Decimal(amount)
            
            # SAVING TRANSACTION HISTORY
            trans_ref_code = randint(1000000, 2999999999)
            trans_ref_code_2 = randint(100, 299)
            transaction = TransferHistory()
            transaction.ref_code = f'TRS-{trans_ref_code}-{trans_ref_code_2}'
            transaction.account = account
            transaction.sender = sender
            transaction.receiver = receiver
            transaction.transfer_type = transfer_type
            transaction.transaction_type = transaction_type
            transaction.receiver_bank_name = receiver_bank_name
            transaction.amount = decimal_amount
            transaction.fee = fee
            transaction.status = status
            transaction.save()
            print("i am working")
            # email = account.email
            # balance = client.balance
            # message = f"Dear {account.first_name}, \n\nYour wallet was credited ${profit} as a profit from your auto-trade. \n\nNew balance: {balance}"
            # send_mail(email, message)
            messages.success(
                request, f'You have added the TRANSACTION HISTORY of ${decimal_amount} to {account.first_name} account successfully! ')
        return redirect('user_profile', id=account.id)
    form = TransactionsForm()
    context = {
        'form': form
    }
    return render(request, 'backend/add_transaction.html', context)



@login_required(login_url='login')
@user_passes_test(is_admin)
def update_history(request, id):
    transaction = TransferHistory.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateHistoryForm(request.POST, instance=transaction)
        # print(f'I got here {form}')
        if form.is_valid():
            form.save()
            account = transaction.account
            # referrer = account.referred_by
            # print(f'this is the referrer: {referrer}')
            
            messages.success(
                    request, f'You have updated a TRANSACTION HISTORY This account successfully! ')
            return redirect('user_profile', id=account.id)
        else:
            messages.error(
                    request, f'Invalid Operation! ')
            return redirect('user_profile', id=account.id)
    form = UpdateHistoryForm(instance=transaction)
    context = {
        'form': form,
        'transaction': transaction
    }
    return render(request, 'backend/update_history.html', context)



@login_required(login_url='login')
@user_passes_test(is_admin)
def investment(request, id):
    if request.method == 'POST':
        form = CreditorForm(request.POST)
        print(f'I got here {form}')
        if form.is_valid():
            account = Account.objects.get(id=id)
            
            print("form is valid")
            amount = form.cleaned_data['amount']
            invested_amount = Decimal(amount)
            account.invested += invested_amount
            account.balance += invested_amount
            print(amount)
            account.save()
            email = account.email
            balance = account.balance
            subject = 'Fund Wallet'
            message = f"Dear {account.first_name}, \n\nYour INVESTMENT of ${invested_amount} has been processed successfully. \n\nNew balance: {balance}"
            send_mail(email, message, subject)
            messages.success(
                request, f'You have added the INVESTMENT of ${amount} to {account.first_name} account successfully! ')
            return redirect('user_profile', id=account.id)
    return render(request, 'backend/dashboard.html')



@login_required(login_url='login')
@user_passes_test(is_admin)
def available(request, id):
    if request.method == 'POST':
        form = CreditorForm(request.POST)
        print(f'I got here {form}')
        if form.is_valid():
            account = get_object_or_404(Account, id=id)
            print("form is valid")
            amount = form.cleaned_data['amount']
            available_bal = Decimal(amount)
            account.available_balance = available_bal
            account.save()
            messages.success(
                request, f'You have added ${amount} to {account.first_name}  BALANCE successfully! ')
            return redirect('user_profile', id=account.id)
        else:
            messages.success(
                request, f'Something went wrong, try again later')
            return redirect('user_profile', id=account.id)
            
    return render(request, 'backend/dashboard.html')



@login_required(login_url='login')
@user_passes_test(is_admin)
def countdown(request, id):
    account = get_object_or_404(Account, id=id)
    if request.method == 'POST':
        form = CountdownForm(request.POST)
        print(f'I got here {form}')
        if form.is_valid():
            # withdrawal_date = form.cleaned_data['withdrawal_date']
            allow_transfer = form.cleaned_data['allow_transfer']
            # print(withdrawal_date)
            # account.withdrawal_date = withdrawal_date
            account.allow_transfer = allow_transfer
            account.save()
            messages.success(
                request, f"You have change {account.first_name}'s account status successfully! ")
        return redirect('user_profile', id=account.id)
    return render(request, 'backend/dashboard.html')




@login_required(login_url='login')
@user_passes_test(is_admin)
def pending_transactions(request):
    transactions = Transactions.objects.all()
    
    context = {
        'transactions': transactions,
    }
    return render(request, 'backend/pending_transactions.html', context)









@login_required(login_url='login')
@user_passes_test(is_admin)
def pending_withdrawal(request):
    transactions = Transactions.objects.all()
    
    context = {
        'transactions': transactions,
    }
    return render(request, 'backend/pending_withdrawal.html', context)






def send_mail(email, message, subject):
    # ==========================ZOHO MESSAGE NOTIFY USER===============================
    recipient = email
    mail_subject = subject
    

    # create message
    msg = MIMEText(message)
    msg['Subject'] = mail_subject
    msg['From'] = sender
    msg['To'] = recipient

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

    # Perform operation via server
    server.login(sender, sender_password)
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()
    



def add_user(request):
    acc_no = random.randint(2111111111, 2999999999)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            country = form.cleaned_data['country']
            email = form.cleaned_data['email']
            # phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            acc_number = acc_no
            # reg_number=form.cleaned_data['reg_number']
            user = Account.object.create_user(acc_number=acc_number, first_name=first_name, last_name=last_name, country=country,
                                               email=email, password=password, )
            
            user.is_active = True
            user.save()
            user_pin = Pin()
            pin = randint(1111, 9999)
            user_pin.account = user
            user_pin.pin = pin
            user_pin.save()
            messages.success(request, f'You have created a User with the name, {first_name} {last_name}.')
            return redirect('user_profile', id=user.id)
        else:
            messages.success(request, 'Invalid Registration Form. Registration failed.')
            return redirect('client_list')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'backend/client_list.html', context)




    # ========================== UPDATE USER===============================


@login_required(login_url='login')
@user_passes_test(is_admin)
def edit_user(request, id):
    try:
        user_to_edit = Account.object.get(id=id)
    except Account.DoesNotExist:
        # Handle the case where the student with the given id does not exist
        messages.error(request, 'User not found.')
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user_to_edit)
        if form.is_valid():
            updated_user = form.save()  # Save the updated data to the existing property instance

            messages.success(
                request, f'Student with the name "{updated_user.first_name}" has been updated.')
            return redirect('user_profile', id=user_to_edit.id)
        else:
            messages.error(
                request, 'Invalid Student Form Submitted. Update Failed.')
    else:
        form = UserForm(instance=user_to_edit)

    context = {
        'user_form': form,
        'user_to_edit': user_to_edit,
    }
    return render(request, 'backend/edit_user.html', context)








@login_required(login_url='login')
@user_passes_test(is_admin)
def package_delete(request, id):
    package = Package.objects.get(id=id)
    package.delete()
    messages.success(request, f'You have DELETED package successfully')

    return redirect('packages')

# Deleting user
@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_user(request, id):
    client = Account.object.get(id=id)
    client.delete()
    messages.success(request, f'You have DELETED User successfully')

    return redirect('client_list')

# Deleting user
@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_history(request, id):
    history = TransferHistory.objects.get(id=id)
    client = history.account
    history.delete()
    messages.success(request, f'You have DELETED User successfully')

    return redirect('user_profile', id=client.id)


# Deleting user
@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_proof(request, id):
    proof = Payment.objects.get(id=id)
    proof.delete()
    messages.success(request, f'You have DELETED User successfully')

    return redirect('proof')



import requests

def btc_update(request):
    if request.method == 'POST':
        form =BtcForm(request.POST)
        if form.is_valid():
            
            update = form.cleaned_data['update']
            try:
                url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
                headers = {'X-CoinAPI-Key': '897F7552-BA92-498D-9C09-EAE790794903'}
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Raise an exception for any HTTP errors
                data = response.json()
                rate = data['rate']
                price = round(rate, 2)
                btc_price = get_object_or_404( Btc, id=1)
                btc_price.price = price
                btc_price.save()
                messages.success(request, f'BTC Price Updated successfully!')
                return redirect('admin_dashboard')
            except requests.exceptions.RequestException as e:
                # Handle the error gracefully
                print(f"Error fetching BTC data: {e}")
                return redirect('admin_dashboard')
            except Exception as e:
                # Handle any other unexpected exceptions
                print(f"An unexpected error occurred: {e}")
                return redirect('admin_dashboard')