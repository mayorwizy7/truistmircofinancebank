from django.shortcuts import render, redirect
from accounts.models import Contact
from accounts.forms import ContactForm

# Email sending 
import smtplib
from email.mime.text import MIMEText
from django.contrib import messages, auth
import random 

zoho_sender2 = 'no-reply@wealthwave.cc'
zoho_sender = 'no-reply@wealthwave.cc'
zoho_password = 'Wealthwave1$'

def home(request):
    # templates = ['home2.html', 'home3.html']
    # random_template = random.choice(templates)
    return render(request, 'home.html')

def features(request):
    # templates = ['home2.html', 'home3.html']
    # random_template = random.choice(templates)
    return render(request, 'features.html')



def contact(request):
    if request.method == 'POST':
        message_form = ContactForm(request.POST)
        if message_form.is_valid():
            name = message_form.cleaned_data['name']
            email = message_form.cleaned_data['email']
            subject = message_form.cleaned_data['subject']
            message = message_form.cleaned_data['message']

            contact = Contact(
                name=name, email=email, subject=subject, message=message)
            contact.save()

            # ==========================ZOHO MESSAGE NOTIFY ADMIN===============================

            recipient = 'support@wealthwave.cc'
            mail_subject = "New Message from Wealth Wave Bank"
            message1 = f"Sender's Name: {name} \n\n Sender's Email: {email} \n\n Subject: {subject} \n\n Message: {message}"

            # create message
            msg = MIMEText(message1)
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
                request, 'Your Message was successfully sent')
            return redirect('contact')
        else:
            messages.error(
                request, 'Something went wrong. Please try again')
            return redirect('contact')

    else:
        message_form = ContactForm()
    context = {
        'message_form': message_form,
    }
    return render(request, 'contact.html', context)




def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')



def faq(request):
    return render(request, 'faq.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms(request):
    return render(request, 'terms.html')


def refund(request):
    return render(request, 'refund.html')


def fees(request):
    return render(request, 'fees.html')


def license(request):
    return render(request, 'license.html')


def all_accounts(request):
    return render(request, 'all_accounts.html')


def personal(request):
    return render(request, 'personal.html')


def business(request):
    return render(request, 'business.html')


def account_current(request):
    return render(request, 'account_current.html')


def cards(request):
    return render(request, 'cards.html')


def loan_home(request):
    return render(request, 'loan_home.html')


def team(request):
    return render(request, 'team.html')


def career(request):
    return render(request, 'career.html')


def testimonials(request):
    return render(request, 'testimonials.html')

def custom_404_page(request, exception):
    return render(request, '404.html', status=404)