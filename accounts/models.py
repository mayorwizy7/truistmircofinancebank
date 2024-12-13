from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from shortuuid.django_fields import ShortUUIDField
from phonenumber_field.modelfields import PhoneNumberField
from . countries import countries, currency_symbols_tuple





# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, acc_number, first_name,  country, last_name, email, password=None):
        if not acc_number:
            raise ValueError(
                'The systen has failed to generate an account number at this time.')
        user = self.model(
            acc_number=acc_number,
            first_name=first_name,
            last_name=last_name,
            # phone=phone,
            country=country,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, country, email, acc_number, password):
        user = self.create_user(
        acc_number=acc_number,
        first_name=first_name,
        last_name=last_name,
        # phone=phone,
        country=country,
        email=email,
        password=password
    )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    username = None
    acc_number = models.CharField( max_length=10, unique=True, verbose_name='Account Number',)
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email Address')
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=50, null=True,
                              blank=True, choices=gender_choice)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, verbose_name='Country', choices=countries)
    profile_pic = models.ImageField(null=True, blank=True, default='profile_photos/default.png', upload_to='profile_photos')
    open_pass = models.CharField(max_length=100, null=True, blank=True, )
    
    # account balances
    available_balance = models.DecimalField(decimal_places=2, max_digits=12, default=0, verbose_name='Available Balance', help_text='Client Cleared Account Balance')
    ledger_balance = models.DecimalField(decimal_places=2, max_digits=12, default=0,verbose_name='Ledger Balance', help_text='Client Uncleared Account Balance')
    wallet = models.DecimalField(decimal_places=2, max_digits=12, default=0, verbose_name='Wallet Balance', help_text='Client wallet Balance')
    last_received = models.DecimalField(decimal_places=2, max_digits=12, default=0, verbose_name='Wallet Balance', help_text='Client wallet Balance')
    account_limit = models.IntegerField(null=True, blank=True, verbose_name='Account Limit')
    currency = models.CharField(max_length=20, default='$', choices=currency_symbols_tuple)

    # required
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    allow_transfer = models.BooleanField(default=False, help_text='Enable or Disable Transfer  (If Disabled, user account will freeze.)')
    is_active = models.BooleanField(default=False, help_text='Enable or disable User. (If disabled, the user cannot login.)')
    is_admin = models.BooleanField(default=False, help_text='If Enabled, user will be able to login into this admin area with almost all permissions.')
    is_staff = models.BooleanField(default=False, help_text='If Enabled, user will be able to login into this admin area with limitations.')
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'acc_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'country']

    object = MyAccountManager()

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f'{self.first_name} {self.last_name} (Account Number: {self.acc_number})'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True



class Pin(models.Model):
    account = models.OneToOneField(Account, null=True, blank=True, on_delete=models.CASCADE)
    pin = models.IntegerField()
    
    
    def __str__(self):
        return str(self.account)


# Account Statement and Transfer history


class OtherAccounts(models.Model):
    CURRENCY_CHOICES = (
        ('Dollar', 'Dollar'),
        ('Pounds', 'Pounds'),
    )
    
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    acc_number = models.CharField( max_length=10, unique=True, verbose_name='Account Number',)
    
    # account balances
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0, verbose_name='Available Balance', help_text='Client Cleared Account Balance')
    ledger_balance = models.DecimalField(decimal_places=2, max_digits=12, default=0,verbose_name='Ledger Balance', help_text='Client Uncleared Account Balance')
    last_received = models.DecimalField(decimal_places=2, max_digits=12, default=0, verbose_name='Wallet Balance', help_text='Client wallet Balance')
    currency = models.CharField(null=True, blank=True, max_length=15, choices=CURRENCY_CHOICES)
    allow_transfer = models.BooleanField(default=False, help_text='Enable or Disable Transfer  (If Disabled, user account will freeze.)')

    
    

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return str(self.account)
    


class Beneficiary(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('Euro', 'Euro'),
    )
    
    TYPE_CHOICES = (
        ('Internal', 'Internal'),
        ('Local', 'Local'),
        ("Int'l", "Int'l"),
    )
    
    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    acc_name = models.CharField(null=True, blank=True, max_length=50, )
    bank = models.CharField(null=True, blank=True, max_length=50, )
    type = models.CharField(null=True, blank=True, max_length=15, choices=TYPE_CHOICES, default="OWN BANK")
    acc_number = models.CharField( max_length=20, unique=True, verbose_name='Account Number',)
    rout_number = models.CharField(null=True, blank=True, max_length=9, verbose_name='Routing Number',)
    swift_code = models.CharField(null=True, blank=True, max_length=20, )
    currency = models.CharField(null=True, blank=True, max_length=15, choices=CURRENCY_CHOICES, default="USD")
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(null=True, blank=True, max_length=50, choices=countries, default='UNITED STATES' )
    image = models.ImageField(null=True, blank=True, default='profile_photos/default.png', upload_to='beneficiary_photos')

    # account balances
    

    
    

    class Meta:
        verbose_name = 'Beneficiary'
        verbose_name_plural = 'Beneficiaries'

    def __str__(self):
        return str(self.account)
    
    

class TransferHistory(models.Model):
    STUTUS = (
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Failed', 'Failed'),
    )
    TRANSACTION_TYPES = (
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
        ('Card', 'Card'),
        ('Deposit', 'Deposit'),
    )
    TRANSFER_TYPES = (
        ('Internal', 'Internal'),
        ('Local', 'Local'),
        ("Int'l", "Int'l"),
    )

    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    ref_code = models.CharField(null=True, max_length=50)
    sender = models.CharField(max_length=50, verbose_name="Sender's Account Number",)
    receiver = models.CharField(max_length=50, verbose_name="Receiver's Account Number",)
    receiver_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Receiver's Account Name",)
    remark = models.CharField(null=True, blank=True, max_length=100)
    transaction_type = models.CharField(null=True, max_length=15, verbose_name='Type of Transaction', choices=TRANSACTION_TYPES)
    transfer_type = models.CharField(null=True, max_length=15, verbose_name='Transfer Type', choices=TRANSFER_TYPES)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    receiver_routing_number = models.CharField(max_length=255, null=True, blank=True)
    receiver_IBAN = models.CharField(max_length=255, null=True, blank=True)
    receiver_bank_name = models.CharField(max_length=255, null=True, blank=True)
    receiver_bank_address = models.CharField(max_length=255, null=True, blank=True)
    receiver_bank_country = models.CharField(max_length=255, null=True, blank=True)
    transaction_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(null=True, blank=True, max_length=15, choices=STUTUS)
    fee = models.CharField(max_length=100, null=True, blank=True, default="Free" )
    
    

    class Meta:
        verbose_name = 'Transfer History'
        verbose_name_plural = 'Transfer Histories'

    def __str__(self):
        return str(self.sender)
    
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ FDR Plan FORM MODEL +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class FDR_plan(models.Model):
    PLANS = (
        ('Entrepreneur Extra', 'Entrepreneur Extra'),
        ('Platinum FDR', 'Platinum FDR'),
        ('Revenue Fighters', 'Revenue Fighters'),
    )

    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    plan = models.CharField(null=True, max_length=50, choices=PLANS)
    request_date = models.DateTimeField(default=timezone.now)
    
    

    class Meta:
        verbose_name = 'FDR Plan'
        verbose_name_plural = 'FDR Plans'

    def __str__(self):
        return str(self.account)
    
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ FDR Plan FORM MODEL +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class DSP_plan(models.Model):
    PLANS = (
        ('Education Savings', 'Education Savings'),
        ('Tour Plan', 'Tour Plan'),
        ('Marraige Plan', 'Marraige Plan'),
    )

    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    plan = models.CharField(null=True, max_length=50, choices=PLANS)
    request_date = models.DateTimeField(default=timezone.now)
    
    

    class Meta:
        verbose_name = 'DSP Plan'
        verbose_name_plural = 'DSP Plans'

    def __str__(self):
        return str(self.account)
    
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Loan Plan FORM MODEL +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Loan_plan(models.Model):
    PLANS = (
        ('Rural Development', 'Rural Development'),
        ('Car Loan', 'Car Loan'),
        ('Farmer loan', 'Farmer loan'),
    )

    account = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    plan = models.CharField(null=True, max_length=50, choices=PLANS)
    request_date = models.DateTimeField(default=timezone.now)
    
    

    class Meta:
        verbose_name = 'Loan Plan'
        verbose_name_plural = 'Loan Plans'

    def __str__(self):
        return str(self.account)




# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++ CONTACT FORM MODEL +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=False)
    message = models.TextField(max_length=1000, null=False)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return str(self.name)
    



class OTP(models.Model):
        user = models.ForeignKey(Account, on_delete=models.CASCADE)
        time_stamped = models.DateTimeField(auto_now_add=True)
        otp = models.IntegerField()
        
        
        
        
CARD_TYPE = (
    ("Master", "Master"),
    # ("Visa", "Visa"),
    # ("Verve", "Verve"),

)        


class CreditCard(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    card_id = ShortUUIDField(unique=True, length=5, max_length=20, prefix="CARD", alphabet="1234567890")

    name = models.CharField(max_length=50)
    number = models.BigIntegerField()
    expiry = models.DateField()
    cvv = models.IntegerField()

    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, null=True, blank=True)

    card_type = models.CharField(choices=CARD_TYPE, max_length=20, default="Master")
    card_status = models.BooleanField(default=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"