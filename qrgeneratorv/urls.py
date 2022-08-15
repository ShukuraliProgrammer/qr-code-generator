from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('qrcode-list', views.qrcodes_list, name='qrcodes-list'),
   path('template-list/', views.qr_template_list,name='template-list'),
   path('qrcode-detail/<int:pk>/', views.qrcode_detailView, name='qrcode_detail'),
   path('qrcode-delete/<int:pk>/', views.qrcode_deleteView,name='qrcode_delete'),
   path('qr-website-create', views.webiste_url_create,name='website_url_create'),
   # path('register/', views.registerview,name='registerview'),
   path('login/', views.login_user,name='login_user'),
   path('logout/', views.logoutView,name='logoutView'),
   
   path('qr-url/<int:pk>/', views.qr_url, name='QrUrl'),

   path('social_new_create', views.tmp_social_new_create, name='social_media_create'),
   path('phone-detail/<int:pk>/', views.phoneDetailViews, name='PhoneDetail'),
   path('pdf_create', views.tmp_pdf_create, name='pdf_create'), 

   path('free_web/', views.free_web_url_create, name='free_web_url_create'),
   path('qr-style/', views.qrcodestyle, name='qr_style'),
   path('social_media_type_1_url_counter/<int:pk>/', views.qrcode_social1_url_counter, name='social_media_type_1_url_counter'), 
   path('social_media_type_2_url_counter/<int:pk>/', views.qrcode_social2_url_counter, name='social_media_type_2_url_counter'), 
   path('social_media_type_3_url_counter/<int:pk>/', views.qrcode_social3_url_counter, name='social_media_type_3_url_counter'), 


]