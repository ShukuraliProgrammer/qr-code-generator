from django.urls import path
from . import views

urlpatterns = [
   path('', views.qrcodes_list, name='qrcodes-list'),
   path('template-list/', views.qr_template_list,name='template-list'),
   path('qrcode-detail/<int:pk>/', views.qrcode_detailView, name='qrcode_detail'),
   path('qrcode-delete/<int:pk>/', views.qrcode_deleteView,name='qrcode_delete'),
   path('qr-webiste-create', views.webiste_url_create,name='website_url_create'),
   
   path('qr-url/<int:pk>', views.qr_url, name='QrUrl'),

  
   path('social_new_create', views.tmp_social_new_create, name='social_media_create'),
   path('phone-detail/<int:pk>/', views.phoneDetailViews, name='PhoneDetail'),
   path('pdf_create', views.tmp_pdf_create, name='pdf_create'),
   path('rating-create', views.tmp_rating_create, name='rating_create'),   
]