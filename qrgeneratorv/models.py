

from django.db import models
import qrcode

from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random
class Tariff(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тарифа')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    expires_in = models.DateTimeField('Истекает', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

class QrCode(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название QR кода')
    url=models.CharField(max_length=100,verbose_name='URL')
    image=models.FileField(upload_to='qrcode',blank=True)
    expires_in = models.DateTimeField('Истекает', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url_counter = models.IntegerField("Scaner Counts",default=0,null=True,blank=True)
    def save(self,*args,**kwargs):
        print("This is model id ",self.id)
        qrcode_img = qrcode.make('10.10.1.89:8000/qr-url/{}'.format(self.id))
        canvas=Image.new("RGB", (300,300),"white")
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer=BytesIO()
        canvas.save(buffer,"PNG")
        self.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.url
    



class SocialMediaChannels(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название',default='Название')
    url = models.URLField(verbose_name='Ссылка')
    text = models.TextField(verbose_name='Текст')
    def __str__(self):
        return self.text


class Template(models.Model):
    qrname = models.CharField(max_length=100, verbose_name='Название')
    color_primary = models.CharField(max_length=7, verbose_name='Основной цвет', null=True, blank=True)
    color_button = models.CharField(max_length=7, verbose_name='Цвет кнопки',null=True, blank=True)
    image = models.ImageField(upload_to = 'templates', verbose_name='Изображение',null = True, blank = True)
    headline = models.CharField(max_length=100, verbose_name='Заголовок', null=True, blank=True)
    about_us = models.TextField(max_length=100, verbose_name='О нас', null=True, blank=True)
    social_media_type = models.CharField(max_length=100, verbose_name='Тип медиа1',null=True,blank=True)
    title1 = models.CharField(max_length=100, verbose_name='Название',default='Название',null=True,blank=True)
    url1 = models.CharField(max_length=100, verbose_name='Ссылка',null=True,blank=True)
    social_media_type2 = models.CharField(max_length=100, verbose_name='Тип медиа2',null=True,blank=True)
    title2 = models.CharField(max_length=100, verbose_name='Название',default='Название',null=True,blank=True)
    url2 = models.CharField(max_length=100,verbose_name='Ссылка',null=True,blank=True)
    social_media_type3 = models.CharField(max_length=100, verbose_name='Тип медиа3',null=True,blank=True)
    title3 = models.CharField(max_length=100, verbose_name='Название',default='Название',null=True,blank=True)
    url3 = models.CharField(max_length=100,verbose_name='Ссылка',null=True,blank=True)
    add_more = models.CharField(max_length=100, verbose_name='Дополнительно',null=True,blank=True)
    welcome_screen = models.ImageField(upload_to = 'templates', verbose_name='Экран приветствия',null=True, blank=True)
    feadback = models.TextField(verbose_name='Отзывы',null=True, blank=True)
    imageforqr = models.ImageField(upload_to = 'templates', verbose_name='Изображение для QR',null=True, blank=True)
    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'


       
    
class Comment(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
