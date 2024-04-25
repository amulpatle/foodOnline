from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def detectUser(user):
    if  user.role == 1:
        redirectUrl = 'vendorDashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl = 'custDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl
    
def send_verification_email(request,user):
    current_site = get_current_site(request)
    mail_subject = 'please activate your account'
    message = render_to_string('accounts/emails/account_verification_email.html',{
        'user':user,
        'domain':current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
    })