import random
from .forms import TemplateForm
from django.shortcuts import redirect, render
from .models import QrCode, Template
from django.db.models import Count
import qrcode
from django.core.files import File
from io import BytesIO
from PIL import Image, ImageDraw


def qrcodes_list(request):
    qr_code=QrCode.objects.all().order_by('-created_at')
    return render(request,"qrcodes-list.html",{'qr_code':qr_code})

def qr_template_list(request):
    return render(request,"tmp_list.html")

def qrcode_detailView(request,pk):
    qr_code=QrCode.objects.get(id=pk)
    return render(request,"qrcode-detail.html",{'qr':qr_code})

def qrcode_deleteView(request,pk):
    qr_code=QrCode.objects.get(id=pk)
    qr_code.delete()
    return redirect('qrcodes-list')


def webiste_url_create(request):
    context={}
    if request.method == "POST":
        Url=request.POST['url']
        qr_obj = QrCode.objects.create(url=Url)
        qr_obj.save()
        return redirect('qrcodes-list')
    return render(request,"tmp_website.html",context=context)


def qr_url(request,pk):
    qr_code=QrCode.objects.get(id=pk)
    qr_code.url_counter += 1
    qr_code.save()
    return redirect(qr_code.url)


def tmp_social_new_create(request):
    context={}
    if request.method == "POST":
        form  = TemplateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            qrcode_img = qrcode.make('10.10.1.89:8000/phone-detail/{}'.format(form.instance.id))
            print("This is qrcode",qrcode_img)
            canvas=Image.new("RGB", (200,200),"black")
            print("This is canvas", canvas)
            draw=ImageDraw.Draw(canvas)
            print("This is draw", draw)
            canvas.paste(qrcode_img)
            buffer=BytesIO()
            canvas.save(buffer,"PNG")
            print("Test")
            obj1 = QrCode()
            obj1.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
            obj1.url = f'/phone-detail/{form.instance.id}'
            obj1.save()
            print(f"Test2--->{obj1.url} -- {obj1.image}")
            canvas.close()
            return redirect('qrcodes-list')
        return redirect('template-list')
    context = {
        'form':TemplateForm()
    }
    return render(request,"tmp_social.html",context=context)

def phoneDetailViews(request,pk):
    qr_code=Template.objects.get(id=pk)

    return render(request,"phone-detail.html",{'qr':qr_code})
    

def tmp_pdf_create(request):
    context={}
    if request.method == "POST":
        form  = TemplateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            redirect('QrCode')
        return redirect('QRTemplateList')
    context = {'form': TemplateForm()}
    return render(request,"pdf_create.html",context=context)


def tmp_rating_create(request):
    context={}
    if request.method == "POST":
        form  = TemplateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            redirect('QrCode')
        return redirect('QRTemplateList')
    context = {'form': TemplateForm()}
    return render(request,"rating_create.html",context=context)

def tmp_mp3music_create(request):
    context={}
    if request.method == "POST":
        form  = TemplateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            redirect('QrCode')
        return redirect('QRTemplateList')
    context = {'form': TemplateForm()}
    return render(request,"mp3music_create.html",context=context)