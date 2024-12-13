from django.urls import path
from . import views

urlpatterns = [
    path('client_list/', views.client_list, name='client_list'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('kyc_admin/', views.kyc_admin, name='kyc_admin'),
    path('kyc_details/<str:id>/', views.kyc_details, name='kyc_details'),
    path('kyc_update/<str:id>/', views.kyc_update, name='kyc_update'),
    path('user_profile/<str:id>/', views.user_profile, name='user_profile'),
    path('edit_user/<str:id>/', views.edit_user, name="edit_user"),

    path('add_profit/<str:id>/', views.add_profit, name='add_profit'),
    path('add_bonus/<str:id>/', views.add_bonus, name='add_bonus'),
    path('investment/<str:id>/', views.investment, name='investment'),
    path('available/<str:id>/', views.available, name='available'),
    path('countdown/<str:id>/', views.countdown, name='countdown'),
    path('auto_add_profit/', views.auto_add_profit, name='auto_add_profit'),
    path('clear_user/<str:id>/', views.clear_user, name='clear_user'),
    path('update_history/<str:id>/', views.update_history, name='update_history'),
    # path('add_user', views.add_user, name='add_user'),
    path('add_transaction/<str:id>/', views.add_transaction, name='add_transaction'),
    path('add_user/', views.add_user, name='add_user'),
    path('pending_transactions/', views.pending_transactions, name='pending_transactions'),
    path('pending_withdrawal/', views.pending_withdrawal, name='pending_withdrawal'),
    path('proof/', views.proof, name='proof'),
    path('packages/', views.packages, name='packages'),
    path('update_packages/<str:id>/', views.update_packages, name='update_packages'),
    path('add_packages/', views.add_packages, name='add_packages'),
    path('package_delete/<str:id>/', views.package_delete, name='package_delete'),
    path('delete_user/<str:id>/', views.delete_user, name='delete_user'),
    path('delete_proof/<str:id>/', views.delete_proof, name='delete_proof'),
    path('delete_history/<str:id>/', views.delete_history, name='delete_history'),
    path('btc_update/', views.btc_update, name='btc_update'),
    
]
