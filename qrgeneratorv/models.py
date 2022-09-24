
from operator import mod
from django.db import models
import qrcode
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,Group
from shutil import copy
import os
import png
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random
from qrgeneratorv.managers import UserManager
import pyqrcode
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
DEVICE_TYPES = [
    "mobile",  
    "tablet",
    "touch_capable",
    "pc",
    "bot",
    "other"
]

class User(AbstractBaseUser, PermissionsMixin):
    tariff = models.ForeignKey('Tariff', on_delete=models.CASCADE, related_name='users',default=1)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    # Required fields
    data_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
       
        send_mail(
            'This is beat task',
            f"Assalomu Alaykum {self.first_name} sizni QrCode Generator site ga obuna bulganingiz bilan tabriklaymiz",
            "shukurdev2002@gmail.com",
            ["shukuralijob@gmail.com"],
            fail_silently=False,
            )
        super().save(*args, **kwargs)

    
SCALE_OPTIONS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)

COLOR_OPTIONS = (
    ('black', 'black'),
    ('red', 'red'),
    ('blue', 'blue'),
    ('green', 'green'),
    ('brown', 'brown'),
    ('purple', 'purple'),
    ('pink', 'pink'),
    ('yellow', 'yellow'),
    ('grey', 'grey'),
    ('light_blue', 'light_blue'),
)

OUTPUT_OPTIONS = (
    ('SVG', 'SVG'),
    ('EPS', 'EPS'),
    ('PNG', 'PNG'),
)

        

class Tariff(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тарифа')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text="Ценa в долларах")
    expires_in = models.DurationField('Истекает', null=True, blank=True,help_text="по дням")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sms_service = models.IntegerField(verbose_name='Сервис отправки SMS',help_text='Date of SMS Cervice')
    admin_panel = models.BooleanField(default=False, verbose_name='Админ панель')
    editing_count = models.IntegerField(verbose_name='Количество редактирований', default=0)
    scan_count = models.IntegerField(verbose_name='Количество сканирований',help_text='Count of Scan',blank = True, null = True)
    creation_count = models.IntegerField(verbose_name='Количество созданий',help_text='Count of Creation',default= 0)
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

class QrCode(models.Model):
    DEVICE_TYPES = [ 
        (device_type, device_type) for device_type in DEVICE_TYPES
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qrcodes',null=True, blank=True)
    template = models.OneToOneField('Template', on_delete=models.CASCADE,related_name='qrcodes',null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Название QR кода')
    url=models.CharField(max_length=100,verbose_name='URL',null=True,blank=True)
    image=models.FileField(upload_to='qrcode',blank=True,null=True)
    expires_in = models.DateTimeField('Истекает', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url_counter = models.IntegerField("Scaner Counts",default=0,null=True,blank=True)
    scale = models.CharField(blank = False, null = False, max_length=2, choices=SCALE_OPTIONS, default=5)
    color = models.CharField(blank = False, null = False, max_length=15, choices=COLOR_OPTIONS, default='black')
    device = models.CharField(max_length=64, choices=DEVICE_TYPES, null=True, blank=True, default='other')
    android = models.IntegerField("Android",default=0,null=True,blank=True)
    ios = models.IntegerField("iOS",default=0,null=True,blank=True)
    os = models.IntegerField("OS",default=0,null=True,blank=True)
    mobile = models.IntegerField("Mobile",default=0,null=True,blank=True)
    other_devices = models.IntegerField("Other Devices",default=0,null=True,blank=True)
    # def save(self,*args,**kwargs):
    #     print("This is model id ",self.id)
    #     qrcode_img = qrcode.make('10.10.1.89:8000/qr-url/{}'.format(self.id))
    #     canvas=Image.new("RGB", (300,300),"white")
    #     draw=ImageDraw.Draw(canvas)
    #     canvas.paste(qrcode_img)
    #     buffer=BytesIO()
    #     canvas.save(buffer,"PNG")
    #     self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)

    #     canvas.close()
    #     super().save(*args,**kwargs)
    
    def __str__(self):
        return self.url
    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    admin_photo.short_description = 'QR Code'
    admin_photo.allow_tags = True

class SocialMediaChannels(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название',default='Название')
    url = models.URLField(verbose_name='Ссылка')
    text = models.TextField(verbose_name='Текст')
    def __str__(self):
        return self.text


class Template(models.Model):

    DEVICE_TYPES = [ 
        (device_type, device_type) for device_type in DEVICE_TYPES
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='templates',null=True, blank=True)
    qrname = models.CharField(max_length=100, verbose_name='Название')
    color_primary = models.CharField(max_length=7, verbose_name='Основной цвет', null=True, blank=True)
    color_button = models.CharField(max_length=7, verbose_name='Цвет кнопки',null=True, blank=True)
    image = models.ImageField(upload_to = 'templates', verbose_name='Изображение',null = True, blank = True)
    headline = models.CharField(max_length=100, verbose_name='Заголовок', null=True, blank=True)
    about_us = models.TextField(max_length=100, verbose_name='О нас', null=True, blank=True)
    social_media_type = models.CharField(max_length=100, verbose_name='Тип медиа1',null=True,blank=True)
    title1 = models.CharField(max_length=100, verbose_name='Название',default='Название',null=True,blank=True)
    url1 = models.CharField(max_length=100, verbose_name='Ссылка',null=True,blank=True)
    social_media_type1_url_counter =  models.IntegerField("Тип медиа1 Enter Counts",default=0,null=True,blank=True)
    
    social_media_type2 = models.CharField(max_length=100, verbose_name='Тип медиа2',null=True,blank=True)
    title2 = models.CharField(max_length=100, verbose_name='Название',default='Название',null=True,blank=True)
    url2 = models.CharField(max_length=100,verbose_name='Ссылка',null=True,blank=True)
    social_media_type2_url_counter =  models.IntegerField("Тип медиа2 Enter Counts",default=0,null=True,blank=True)

    social_media_type3 = models.CharField(max_length=100, verbose_name='Тип медиа3',null=True,blank=True)
    title3 = models.CharField(max_length=100, verbose_name='Название',default='Название',null=True,blank=True)
    url3 = models.CharField(max_length=100,verbose_name='Ссылка',null=True,blank=True)
    social_media_type3_url_counter =  models.IntegerField("Тип медиа3 Enter Counts",default=0,null=True,blank=True)
    scale = models.CharField(blank = False, null = False, max_length=2, choices=SCALE_OPTIONS, default=5)
    color = models.CharField(blank = False, null = False, max_length=15, choices=COLOR_OPTIONS, default='black')
    device = models.CharField(max_length=64, choices=DEVICE_TYPES, verbose_name='Тип устройства', null=True, blank=True, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'

    def __str__(self):
        return self.qrname
    
class Comment(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class ForFakeTemplate(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='second_template',null=True, blank=True)
    social_media_type = models.CharField(max_length=100, verbose_name='Тип медиа',null=True,blank=True)
    url = models.CharField(max_length=100, verbose_name='Ссылка')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Ссылка для шаблона'
        verbose_name_plural = 'Ссылки для шаблона'



class SMSNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sms_notifications')
    allscans = models.CharField(max_length=100, verbose_name='Все отсканированные коды')
    os_enter_count = models.IntegerField("ОС Enter Counts",default=0,null=True,blank=True)
    mobile_enter_count = models.IntegerField("Мобильный Enter Counts",default=0,null=True,blank=True)

    class Meta:
        verbose_name = 'СМС оповещение'
        verbose_name_plural = 'СМС оповещения'
    
    def __str__(self):
        return self.user.email



class QRCodeFree(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    content = models.CharField(max_length=500, verbose_name='Enter text or url')
    scale = models.CharField(blank = False, null = False, max_length=2, choices=SCALE_OPTIONS, default=5)
    color = models.CharField(blank = False, null = False, max_length=15, choices=COLOR_OPTIONS, default='black')
    