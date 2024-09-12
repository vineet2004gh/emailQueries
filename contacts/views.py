from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def send_test_email(request):
    message = ""
    
    if request.method == "POST":
        email = request.POST.get('email')
        subject = 'Test Email'
        message = 'This is a test email from Django.'
        email_from = 'vnjain2004@gmail.com'
        recipient_list = [email]
        
        send_mail(subject, message, email_from, recipient_list)
        message = "Email sent successfully to " + email

    return render(request, 'contacts/send_email_form.html', {'message': message})

def send_otp(request):
    message=""
    if request.method=="POST":
        email=request.POST.get('email')
        subject='OTP'
        message= 'The OTP is 343264'
        email_from='vnjain2004@gmail.com'
        recipient_list=[email]
        send_mail(subject,message,email_from,recipient_list)
        message = "OTP Sent!"
    return render(request,'contacts/otp.html',{'message':message})

def contact_form(request):
    return render(request, 'contacts/contact.html')
