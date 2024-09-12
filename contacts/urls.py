from django.urls import path
from .views import send_test_email,contact_form,send_otp

urlpatterns=[
    path('', contact_form, name='contact'), 
    path('send-email/', send_test_email, name='send_email'),
    path('send-otp/',send_otp, name='send_otp'),
]