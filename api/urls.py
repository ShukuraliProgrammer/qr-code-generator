from django.urls import path 
from .views import QrCodeCreate

urlpatterns = [ 
    path('qrcode/', QrCodeCreate.as_view(), name='qrcode_create'),
]

