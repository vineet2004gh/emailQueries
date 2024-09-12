from django.urls import path
from .views import send_test_email,contact_form

urlpatterns=[
    path('', contact_form, name='contact'), 
    path('send-email/', send_test_email, name='send_email'),
]