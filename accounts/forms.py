from django import forms
from .models import Account, Beneficiary, Contact, FDR_plan, DSP_plan, Loan_plan, CreditCard, OtherAccounts


class CreditCardForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Card Holder Name"}))
    # number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Card Number"}))
    # month = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Expiry Month"}))
    # year = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Expiry Month"}))
    # cvv = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"CVV"}))

    class Meta:
        model = CreditCard
        fields = ['card_type']
        
    def __init__(self, *args, **kwargs):
        super(CreditCardForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
    
# ======================Adding money to credit card form==============================
class AmountForm(forms.ModelForm):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"$30"}))
    
    class Meta:
        model = CreditCard
        fields = ['amount']

    

# ======================Registration form==============================
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'country', 'phone', 'currency',  'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['country'].widget.attrs['placeholder'] = 'Country'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['currency'].widget.attrs['value'] = 'Choose Currency'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
class UserSearchForm(forms.Form):
    acc_number = forms.CharField(max_length=100)


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name',
                  'phone', 'email', 'dob', 'currency', 'gender', 'address', 'country', 'profile_pic']
        
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            

class YourForm(forms.Form):
    acc_number = forms.IntegerField()
    receiver = forms.IntegerField()
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    remark = forms.CharField(max_length=50)
    
    def __init__(self, *args, **kwargs):
        super(YourForm, self).__init__(*args, **kwargs)
        self.fields['acc_number'].widget.attrs['placeholder'] = 'Enter Your Account Number'
        self.fields['receiver'].widget.attrs['placeholder'] = 'Enter Destination Account Number'
        self.fields['amount'].widget.attrs['placeholder'] = 'Enter Amount'
        self.fields['remark'].widget.attrs['placeholder'] = 'Enter Description'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            









class AddAccountForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['acc_name', 'bank', 'type', 'acc_number', 'rout_number', 'swift_code', 'currency', 'address', 'country', 'image']
        
        # widgets = {
        #     'dob': forms.DateInput(attrs={'type': 'date'})
        # }

    def __init__(self, *args, **kwargs):
        super(AddAccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['acc_name'].widget.attrs['placeholder'] = 'Enter Account Name'
            self.fields['bank'].widget.attrs['placeholder'] = 'Enter Bank Name'
            self.fields['type'].widget.attrs['placeholder'] = 'Enter Bank Name'
            self.fields['acc_number'].widget.attrs['placeholder'] = 'Choose Bank Locality'
            self.fields['rout_number'].widget.attrs['placeholder'] = 'Enter Routing Number (if available)'
            self.fields['swift_code'].widget.attrs['placeholder'] = 'Enter Swift Code (if available)'
            self.fields['currency'].widget.attrs['placeholder'] = 'Choose Preferred Currency'
            self.fields['address'].widget.attrs['placeholder'] = 'Enter Address'
            self.fields['country'].widget.attrs['placeholder'] = 'Choose Country'
            self.fields['image'].widget.attrs['placeholder'] = 'Choose User Avarter (If any)'
            self.fields[field].widget.attrs['class'] = ' w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'

class EditAccountForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['acc_name', 'bank', 'type', 'acc_number', 'rout_number', 'swift_code', 'address', 'country', 'currency', 'image']

        
        

    def __init__(self, *args, **kwargs):
        super(EditAccountForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            

# ======================Transfer form==============================
class TransferForm(forms.Form):
    pin = forms.IntegerField()
    acc_number = forms.IntegerField()
    receiver = forms.IntegerField()
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    remark = forms.CharField(max_length=50)
    
    def __init__(self, *args, **kwargs):
        super(TransferForm, self).__init__(*args, **kwargs)
        self.fields['acc_number'].widget.attrs['placeholder'] = 'Enter Your Account Number'
        self.fields['receiver'].widget.attrs['placeholder'] = 'Enter Destination Account Number'
        self.fields['amount'].widget.attrs['placeholder'] = 'Enter Amount'
        self.fields['remark'].widget.attrs['placeholder'] = 'Enter Description'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            


# ======================Local Transfer form==============================
class LocalTransferForm(forms.Form):
    pin = forms.IntegerField()
    acc_number = forms.IntegerField()
    receiver = forms.IntegerField()
    receiver_name = forms.CharField(max_length=50)
    bank_name = forms.CharField(max_length=50)
    routing_number = forms.IntegerField()
    amount = forms.FloatField()
    remark = forms.CharField(max_length=50)
    
    
    def __init__(self, *args, **kwargs):
        super(LocalTransferForm, self).__init__(*args, **kwargs)
        self.fields['acc_number'].widget.attrs['placeholder'] = 'Enter Your Account Number'
        self.fields['receiver'].widget.attrs['placeholder'] = 'Enter Destination Account Number'
        self.fields['amount'].widget.attrs['placeholder'] = 'Enter Amount'
        self.fields['remark'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['bank_name'].widget.attrs['placeholder'] = 'Enter Bank Name'
        self.fields['receiver_name'].widget.attrs['placeholder'] = 'Enter Receiver Name'
        self.fields['routing_number'].widget.attrs['placeholder'] = 'Enter Routing Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            
            


# ======================International Transfer form==============================
class IntlTransferForm(forms.Form):
    acc_number = forms.IntegerField()
    receiver = forms.IntegerField()
    receiver_name = forms.CharField(max_length=50)
    bank_name = forms.CharField(max_length=50)
    bank_address = forms.CharField(max_length=200)
    bank_country = forms.CharField(max_length=50)
    swift_code = forms.CharField(max_length=11)
    iban = forms.IntegerField()
    amount = forms.FloatField()
    remark = forms.CharField(max_length=50)
    pin = forms.IntegerField()
    
    
    def __init__(self, *args, **kwargs):
        super(IntlTransferForm, self).__init__(*args, **kwargs)
        self.fields['acc_number'].widget.attrs['placeholder'] = 'Enter Your Account Number'
        self.fields['receiver'].widget.attrs['placeholder'] = 'Enter Destination Account Number'
        self.fields['amount'].widget.attrs['placeholder'] = 'Enter Amount'
        self.fields['remark'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['bank_name'].widget.attrs['placeholder'] = 'Enter Bank Name'
        self.fields['receiver_name'].widget.attrs['placeholder'] = 'Enter Receiver Name'
        self.fields['bank_address'].widget.attrs['placeholder'] = 'Enter Bank Address'
        self.fields['bank_country'].widget.attrs['placeholder'] = 'Enter Bank Country'
        self.fields['iban'].widget.attrs['placeholder'] = 'Enter IBAN'
        self.fields['swift_code'].widget.attrs['placeholder'] = 'Enter Swift Code'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            
            
            


# ======================Change PIN form==============================
class ChangePinForm(forms.Form):
    current_pin = forms.IntegerField()
    new_pin = forms.IntegerField()
    confirm_pin = forms.IntegerField()
    
    
    def __init__(self, *args, **kwargs):
        super(ChangePinForm, self).__init__(*args, **kwargs)
        self.fields['current_pin'].widget.attrs['placeholder'] = 'Enter Your Current PIN'
        self.fields['new_pin'].widget.attrs['placeholder'] = 'Enter New PIN'
        self.fields['confirm_pin'].widget.attrs['placeholder'] = 'Confirm New PIN'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            


class FDRForm(forms.ModelForm):
    class Meta:
        model = FDR_plan
        fields = ['plan']

    def __init__(self, *args, **kwargs):
        super(FDRForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            


class DSPForm(forms.ModelForm):
    class Meta:
        model = DSP_plan
        fields = ['plan']

    def __init__(self, *args, **kwargs):
        super(DSPForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'
            


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan_plan
        fields = ['plan']

    def __init__(self, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'w-full text-sm bg-secondary1/5 dark:bg-bg3 border border-n30 dark:border-n500 rounded-3xl px-3 md:px-6 py-2 md:py-3'