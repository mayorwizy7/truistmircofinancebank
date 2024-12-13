from django.urls import path
from . import views, credit_card



urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transfer/', views.transfer, name='transfer'),
    path('localtransfer/', views.localtransfer, name='localtransfer'),
    path('intltransfer/', views.intltransfer, name='intltransfer'),
    path('profile/', views.profile, name='profile'),
    path('security/', views.security, name='security'),
    path('pay/', views.pay, name='pay'),
    path('search_user/', views.search_user, name='search_user'),
    path('transfer_amount/<str:id>', views.transfer_amount, name='transfer_amount'),
    path('confirm_payment', views.confirm_payment, name='confirm_payment'),
    path('form/', views.form_view, name='form_view'),
    path('transactions/', views.transactions, name='transactions'),
    path('transfer_form/', views.transfer_form, name='transfer_form'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('local_otp_verification/', views.local_otp_verification, name='local_otp_verification'),
    path('local_transfer_form/', views.local_transfer_form, name='local_transfer_form'),
    path('transaction_detail/<str:id>', views.transaction_detail, name='transaction_detail'),
    path('transfer_success/<str:id>', views.transfer_success, name='transfer_success'),
    
    # path('confirmation/', views.confirmation, name='confirmation'),
    path('change_pin/', views.change_pin, name='change_pin'),
    path('add_beneficiary/', views.add_beneficiary, name='add_beneficiary'),
    
    
    # Recipients
    path('add_account/', views.add_account, name='add_account'),
    path('search_user_by_acc_number/', views.search_user_by_acc_number, name='search_user_by_acc_number'),
    path('beneficiaries/', views.beneficiaries, name='beneficiaries'),
    path('edit_beneficiary/<str:id>/', views.edit_beneficiary, name='edit_beneficiary'),
    path('check_account/', views.check_account, name='check_account'),

    path('detail_view/<int:id>/', views.detail_view, name='detail_view'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('change_password/', views.change_password, name='change_password'),
    
        # Credit Card URLS
    path("card/<card_id>/", credit_card.card_detail, name="card-detail"),
    path("all_cards", credit_card.all_cards, name="all_cards"),
    path("fund-credit-card/<card_id>/", credit_card.fund_credit_card, name="fund-credit-card"),
    path("withdraw_fund/<card_id>/", credit_card.withdraw_fund, name="withdraw_fund"),
    path("delete_card/<card_id>/", credit_card.delete_card, name="delete_card"),
]
