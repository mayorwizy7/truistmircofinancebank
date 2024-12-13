"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from . import views
# from django.views.defaults import page_not_found
from environ import Env
env=Env()
Env.read_env()
ENVIRONMENT = env('ENVIRONMENT', default='production')


# from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('faq', views.faq, name='faq'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms', views.terms, name='terms'),
    path('refund', views.refund, name='refund'),
    path('license', views.license, name='license'),
    path('all_accounts', views.all_accounts, name='all_accounts'),
    path('personal', views.personal, name='personal'),
    path('business', views.business, name='business'),
    path('account_current', views.account_current, name='account_current'),
    path('cards', views.cards, name='cards'),
    path('loan_home', views.loan_home, name='loan_home'),
    path('team', views.team, name='team'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('career', views.career, name='career'),
    path('fees', views.fees, name='fees'),
    path('features', views.features, name='features'),
    path('accounts/', include('accounts.urls')),
    path('bakend/', include('backend.urls')),
    # Custom 404 page
    path('404/', views.custom_404_page, name='custom_404'),
] 

# Only serve media files in development environment
if  ENVIRONMENT == "development":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500  = 'accounts.views.E_500'
handler404 = 'accounts.views.E_404'