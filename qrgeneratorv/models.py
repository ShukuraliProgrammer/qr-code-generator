from django.db import models
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
class QrCode(models.Model):
    url=models.URLField()
    image=models.ImageField(upload_to='qrcode',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url_counter = models.IntegerField("Scaner Counts",default=1,null=True,blank=True)
    def save(self,*args,**kwargs):
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
    
