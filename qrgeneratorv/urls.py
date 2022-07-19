from django.urls import path
from . import views

urlpatterns = [
   path('', views.home,name='Home'),
   path('qr-list', views.qr_code,name='QrCode'),
   path('qr-url/<int:pk>', views.qr_url,name='QrUrl'),
   path('qr-detail/<int:pk>/', views.qrcode_detailView,name='QrCodeDetail'),

   
]