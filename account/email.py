from django.conf import settings
from django.core.mail import send_mail

def send_email_user(email, token):
    try:
        
        subject = "Please Verify Your Email"
        message = f'hi plaase click this link http://127.0.0.1:8000/verfiy/{token} to verify your email'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
    except Exception as e:
        return False
    return True