from django import forms
from accounts.models import Account, TransferHistory, Pin, Contact


class CreditorForm(forms.Form):
    amount = forms.FloatField()




class CountdownForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['allow_transfer',
                  ]
        
        # widgets = {
        #     'withdrawal_date': forms.DateInput(attrs={'type': 'date'})
        # }
        
    def __init__(self, *args, **kwargs):
        super(CountdownForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'





# =============================User Update Form==========================
class UserForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False, error_messages={'invalid': ("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = Account
        fields = ['first_name', 'last_name',
                  'phone', 'dob', 'gender', 'email', 'address', 'country', 'profile_pic'
                ]
        widgets = {
                    'dob': forms.DateInput(attrs={'type': 'date'})
                }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            



class TransactionsForm(forms.ModelForm):
    class Meta:
        model = TransferHistory
        fields = ['sender', 'receiver',  'transaction_type', 'transfer_type', 'amount', 
    'receiver_bank_name',  'status', 'fee', 'remark',
]
        
        # widgets = {
        #     'dob': forms.DateInput(attrs={'type': 'date'})
        # }
        
    def __init__(self, *args, **kwargs):
        super(TransactionsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'



class UpdateHistoryForm(forms.ModelForm):
    class Meta:
        model = TransferHistory
        fields = ['status', 'transaction_time']

        widgets = {
            'transaction_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }
        
    def __init__(self, *args, **kwargs):
        super(UpdateHistoryForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'





# ++++++++++++++++++++++++++ ADD USER ++++++++++++++++++++++++++++++++++++++++++
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name',
                   'email', 'country',  'password',  ]
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
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['country'].widget.attrs['placeholder'] = 'Choose Your Country'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'