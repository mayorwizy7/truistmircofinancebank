from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import Account, TransferHistory, Pin, Contact, CreditCard, FDR_plan, DSP_plan, Loan_plan
from django.utils.translation import gettext_lazy as _


class AccountAdmin(UserAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_pic.url))
    fieldsets = (
                (_('Account Details'), {'fields': ('acc_number', 'available_balance', 'ledger_balance', 'wallet', 'allow_transfer', )}),
                
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'email', 'dob', 'gender', 'country', 'address', 'profile_pic' )}),
                
                (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_admin',)}),
        
                (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        
                (_('Security'), {'fields': ('open_pass',)}),
    )
#     add_fieldsets = (
#     (None, {
#         'classes': ('wide',),
#         'fields': ('email', 'first_name', 'last_name', 'password'),
#     }),
# )

    list_display = ('thumbnail', 'acc_number', 'first_name', 'last_name', 'available_balance', 'ledger_balance',
                    'email', 'country', 'is_active', 'last_login')

    search_fields = ('acc_number', 'first_name', 'last_name' 'country',)

    list_display_links = ('acc_number', 'available_balance',
                          'ledger_balance', 'first_name', 'last_name', 'email')
    
    readonly_fields = ('acc_number', 'date_joined', 'last_login', 'open_pass')

    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ('country',)
    list_per_page = 10

# ===============Transaction==============


class TransferHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'ref_code', 'sender',
                    'receiver', 'amount', 'transaction_type', 'transaction_time', )
    list_display_links = ('account', 'ref_code')
    list_per_page = 10
    list_filter = ('transfer_type', 'transaction_type')
    
    search_fields = ('account__first_name', 'account__last_name', 'account__acc_number', 'ref_code', 'sender', 'receiver')


class PinAdmin(admin.ModelAdmin):
    list_display = ('account', 'pin')
    list_display_links = ('account', 'pin')
    list_per_page = 10
    search_fields = ('account__first_name', 'account__last_name', 'account__acc_number', 'pin',)




class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date' )
    list_display_links = ('name', 'email', 'subject', )
    search_fields = ('name', 'email', 'phone_number', 'subject', )
    readonly_fields = ('name', 'email', 'subject', 'message', 'date')
    list_per_page = 10




# class FDRAdmin(admin.ModelAdmin):
#     list_display = ('account', 'plan', 'request_date', )
#     list_display_links = ('account', 'plan', 'request_date', )
#     search_fields = ('account__first_name', 'account__last_name', 'account__acc_number', 'plan', 'request_date', )
#     readonly_fields = ('account', 'plan', 'request_date', )
#     list_per_page = 10




# class DSPAdmin(admin.ModelAdmin):
#     list_display = ('account', 'plan', 'request_date', )
#     list_display_links = ('account', 'plan', 'request_date', )
#     search_fields = ('account__first_name', 'account__last_name', 'account__acc_number', 'plan', 'request_date', )
#     readonly_fields = ('account', 'plan', 'request_date', )
#     list_per_page = 10



# class LoanAdmin(admin.ModelAdmin):
#     list_display = ('account', 'plan', 'request_date', )
#     list_display_links = ('account', 'plan', 'request_date', )
#     search_fields = ('account__first_name', 'account__last_name', 'account__acc_number', 'plan', 'request_date', )
#     readonly_fields = ('account', 'plan', 'request_date', )
#     list_per_page = 10

class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'number',)
    list_display_links = ('name', 'number', )

admin.site.register(Account, AccountAdmin)
admin.site.register(Pin, PinAdmin)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(FDR_plan, FDRAdmin)
# admin.site.register(DSP_plan, DSPAdmin)
# admin.site.register(Loan_plan,LoanAdmin )
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(TransferHistory, TransferHistoryAdmin)
