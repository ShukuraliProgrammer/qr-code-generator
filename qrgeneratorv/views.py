from .forms import TemplateForm, UserForm, UserLoginForm, GenerateQRForm, GenerateQRFree
from django.shortcuts import redirect, render
from .models import QrCode, Template, ForFakeTemplate, QRCodeFree
import qrcode
from django.core.files import File
from django.core.files import File
from io import BytesIO
from PIL import Image, ImageDraw
from django.contrib.auth import authenticate, login, logout
import pyqrcode
from shutil import copy
import os
import png
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,"landing.html")

@login_required(login_url='login_user')
def qrcodes_list(request):
    if request.user.is_authenticated:
        try:
            qr_code=QrCode.objects.filter(user=request.user).order_by('-created_at')
            print(qr_code)
        except:
            return redirect('login_user')
    return render(request,"qrcodes-list.html",{'qr_code':qr_code})

def registerview(request):
    context = {}
    if request.method == "POST":
        form = UserForm(request.POST)
        print("this is form",form)
        if form.is_valid():
            form.save()
            return redirect('login_user')
        return redirect('registerview')
    context = {'form': UserForm()}
    return render(request,"user-email.html",context=context)


from django.contrib import messages
def login_user(request):
    if request.user.is_authenticated:
        return  redirect('template-list')
    else:
        form = UserLoginForm()
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']            
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('template-list')
            else:
                messages.info(request, 'Invalid Username or Password')
                return redirect('login_user')
        else:
            context = {'form': form}
            return render(request, 'login.html', context=context)

@login_required(login_url='login_user')
def logoutView(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login_user')
def qr_template_list(request):
    return render(request,"tmp_list.html")

@login_required(login_url='login_user')
def qrcode_detailView(request,pk):
    qr_code=QrCode.objects.get(id=pk)
    return render(request,"qrcode-detail.html",{'qr':qr_code})


@login_required(login_url='login_user')
def qrcode_deleteView(request,pk):
    qr_code=QrCode.objects.get(id=pk)
    qr_code.delete()
    return redirect('qrcodes-list')


import random
@login_required(login_url='login_user')
def webiste_url_create(request):
    context={}
    user_client = request.user
    user_tariff = user_client.tariff

    if request.method == 'POST' and user_tariff.name == 'Started':
        count_qrcode = QrCode.objects.filter(user=user_client).count()
        if count_qrcode <= 2:
            form = GenerateQRForm(request.POST)
            form.instance.user = request.user
            if form.is_valid():
                form.instance.user = request.user
                QR = form.save()
                qr_code = pyqrcode.create('10.10.1.89:8000/qr-url/{}'.format(form.instance.id))
                if QR.color == 'black':
                    qr_color = (0, 0, 0, 255)
                elif QR.color == 'red':
                    qr_color = (255, 0, 0, 255)
                elif QR.color == 'blue':
                    qr_color = (0, 0, 255, 255)
                elif QR.color == 'green':
                    qr_color = (0, 255, 0, 255)
                elif QR.color == 'brown':
                    qr_color = (150, 75, 0, 255)
                elif QR.color == 'purple':
                    qr_color = (128, 0, 128, 255)
                elif QR.color == 'pink':
                    qr_color = (255, 192, 203, 255)
                elif QR.color == 'yellow':
                    qr_color = (255, 255, 0, 255)
                elif QR.color == 'grey':
                    qr_color = (128, 128, 128, 255)
                elif QR.color == 'light_blue':
                    qr_color = (173, 216, 230, 255)
                else:
                    qr_color = (0, 0, 0, 255)
                qr_code.png("{}.png".format(QR.id), scale=QR.scale, module_color=qr_color)
                copy("{}.png".format(QR.id), "media/qrcode/")
                canvas=Image.open("/home/administrator/DataSiteTechnology/Projects/qr-generator/media/qrcode/{}.png".format(form.instance.id))
                buffer=BytesIO()
                canvas.save(buffer,"PNG")    
                QR.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
                QR.save()
                os.remove("{}.png".format(QR.id))
                return redirect('qrcodes-list')
            else:
                return redirect('website_url_create')
        else:
            return redirect('website_url_create')
    elif request.method == "POST" and user_tariff.name == 'Professional':
        count_qrcode = QrCode.objects.filter(user=user_client).count()
        if count_qrcode <= 50:
            form = GenerateQRForm(request.POST)
            form.instance.user = request.user
            if form.is_valid():
                form.instance.user = request.user
                QR = form.save()
                qr_code = pyqrcode.create('10.10.1.89:8000/qr-url/{}'.format(form.instance.id))
                if QR.color == 'black':
                    qr_color = (0, 0, 0, 255)
                elif QR.color == 'red':
                    qr_color = (255, 0, 0, 255)
                elif QR.color == 'blue':
                    qr_color = (0, 0, 255, 255)
                elif QR.color == 'green':
                    qr_color = (0, 255, 0, 255)
                elif QR.color == 'brown':
                    qr_color = (150, 75, 0, 255)
                elif QR.color == 'purple':
                    qr_color = (128, 0, 128, 255)
                elif QR.color == 'pink':
                    qr_color = (255, 192, 203, 255)
                elif QR.color == 'yellow':
                    qr_color = (255, 255, 0, 255)
                elif QR.color == 'grey':
                    qr_color = (128, 128, 128, 255)
                elif QR.color == 'light_blue':
                    qr_color = (173, 216, 230, 255)
                else:
                    qr_color = (0, 0, 0, 255)
                qr_code.png("{}.png".format(QR.id), scale=QR.scale, module_color=qr_color)
                copy("{}.png".format(QR.id), "media/qrcode/")
                canvas=Image.open("/home/administrator/DataSiteTechnology/Projects/qr-generator/media/qrcode/{}.png".format(form.instance.id))
                buffer=BytesIO()
                canvas.save(buffer,"PNG")    
                QR.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
                QR.save()
                os.remove("{}.png".format(QR.id))
                return redirect('qrcodes-list')
            else:
                return redirect('website_url_create')
        else:
            return redirect('website_url_create')
    elif request.method == "POST" and user_tariff.name == 'Advanced':
        count_qrcode = QrCode.objects.filter(user=user_client).count()
        if count_qrcode <= 250:
            form = GenerateQRForm(request.POST)
            form.instance.user = request.user
            if form.is_valid():
                form.instance.user = request.user
                QR = form.save()
                qr_code = pyqrcode.create('10.10.1.89:8000/qr-url/{}'.format(form.instance.id))
                if QR.color == 'black':
                    qr_color = (0, 0, 0, 255)
                elif QR.color == 'red':
                    qr_color = (255, 0, 0, 255)
                elif QR.color == 'blue':
                    qr_color = (0, 0, 255, 255)
                elif QR.color == 'green':
                    qr_color = (0, 255, 0, 255)
                elif QR.color == 'brown':
                    qr_color = (150, 75, 0, 255)
                elif QR.color == 'purple':
                    qr_color = (128, 0, 128, 255)
                elif QR.color == 'pink':
                    qr_color = (255, 192, 203, 255)
                elif QR.color == 'yellow':
                    qr_color = (255, 255, 0, 255)
                elif QR.color == 'grey':
                    qr_color = (128, 128, 128, 255)
                elif QR.color == 'light_blue':
                    qr_color = (173, 216, 230, 255)
                else:
                    qr_color = (0, 0, 0, 255)
                qr_code.png("{}.png".format(QR.id), scale=QR.scale, module_color=qr_color)
                copy("{}.png".format(QR.id), "media/qrcode/")
                canvas=Image.open("/home/administrator/DataSiteTechnology/Projects/qr-generator/media/qrcode/{}.png".format(form.instance.id))
                buffer=BytesIO()
                canvas.save(buffer,"PNG")    
                QR.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
                QR.save()
                os.remove("{}.png".format(QR.id))
                return redirect('qrcodes-list')
            else:
                return redirect('website_url_create')
        else:
            return redirect('website_url_create')

    context = {'form': GenerateQRForm()}
    return render(request,"tmp_website.html",context=context)


def qr_url(request,pk):
    user_qrcode = QrCode.objects.get(id=pk).user
    user_tariff = user_qrcode.tariff
    qr_code=QrCode.objects.get(id=pk)
    qr_code.url_counter += 1
    if request.user_agent.is_mobile:
        qr_code.mobile += 1
    elif request.user_agent.is_pc:
        qr_code.os += 1
    else:
        qr_code.other += 1
    qr_code.save()
    if user_tariff.name == 'Started':
        if qr_code.url_counter <= 10000:
            return redirect(qr_code.url)
        else:
            return ValueError("You don't have permission to view this page")
    elif user_tariff.name == 'Professional' or user_tariff.name == 'Advanced':
        return redirect(qr_code.url)
    return redirect('qrcodes-list')


def tmp_social_new_create(request):
    context={}
    if request.method == "POST":
        form  = TemplateForm(request.POST, request.FILES)
        user = request.user
        form.instance.user = user
        if form.is_valid():
            form.instance.user = request.user
            if request.FILES:
                form.instance.image = request.FILES['image']
            TMP = form.save()
        
            if form.instance.url1:
                ForFakeTemplate.objects.create(
                    template=form.instance,
                    url=form.instance.url1,
                    social_media_type=form.instance.social_media_type
                )
                form.instance.url1 = f'/social_media_type_1_url_counter/{form.instance.id}'
                form.instance.save()
            if form.instance.url2:
                ForFakeTemplate.objects.create(
                    template=form.instance,
                    url=form.instance.url2,
                    social_media_type=form.instance.social_media_type2
                )
                form.instance.url2 = f'/social_media_type_2_url_counter/{form.instance.id}'
                form.instance.save()
            if form.instance.url3:
                ForFakeTemplate.objects.create(
                    template=form.instance,
                    url=form.instance.url3,
                    social_media_type=form.instance.social_media_type3
                )
                form.instance.url3 = f'/social_media_type_3_url_counter/{form.instance.id}'
                form.instance.save()
            if TMP.color == 'black':
                qr_color = (0, 0, 0, 255)
            elif TMP.color == 'red':
                qr_color = (255, 0, 0, 255)
            elif TMP.color == 'blue':
                qr_color = (0, 0, 255, 255)
            elif TMP.color == 'green':
                qr_color = (0, 255, 0, 255)
            elif TMP.color == 'brown':
                qr_color = (150, 75, 0, 255)
            elif TMP.color == 'purple':
                qr_color = (128, 0, 128, 255)
            elif TMP.color == 'pink':
                qr_color = (255, 192, 203, 255)
            elif TMP.color == 'yellow':
                qr_color = (255, 255, 0, 255)
            elif TMP.color == 'grey':
                qr_color = (128, 128, 128, 255)
            elif TMP.color == 'light_blue':
                qr_color = (173, 216, 230, 255)
            else:
                qr_color = (0, 0, 0, 255)
            TMP.save()
     
            qr_code =pyqrcode.create('10.10.1.89:8000/phone-detail/{}'.format(TMP.id))
            qr_code.png("{}.png".format(TMP.id), scale=TMP.scale, module_color=qr_color)
            copy("{}.png".format(TMP.id), "media/qrcode/")
            canvas=Image.open("/home/administrator/DataSiteTechnology/Projects/qr-generator/media/qrcode/{}.png".format(form.instance.id))
            buffer=BytesIO()
            canvas.save(buffer,"PNG")
            QR = QrCode()
            QR.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
            QR.url = f'/phone-detail/{TMP.id}'
            QR.user= request.user
            QR.name = TMP.qrname
            QR.template = form.instance
            QR.save()
          
           # QrCode.objects.create(url=f'/phone-detail/{TMP.id}', image =QR.image , name=TMP.qrname, user=request.user)
            return redirect('qr_style')
        return redirect('template-list')
    context = {
        'form':TemplateForm()
    }
    return render(request,"tmp_social.html",context=context)


def phoneDetailViews(request,pk):
    qr_code=Template.objects.get(id=pk)

    qrcode1 = QrCode.objects.get(template=qr_code)

    qrcode1.url_counter += 1
    qrcode1.save()
    return render(request,"mobile-tmp-detail.html",{'qr':qr_code})
    
def tmp_pdf_create(request):
    context={}
    if request.method == "POST":
        form  = TemplateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            redirect('QrCode')
        return redirect('QRTemplateList')
    context = {'form': TemplateForm()}
    return render(request,"tmp_pdf.html",context=context)

def qrcode_social1_url_counter(request,pk):
    qr_code=Template.objects.get(id=pk)
    qr_code.social_media_type1_url_counter += 1
    qrformfake = ForFakeTemplate.objects.get(template=qr_code,social_media_type=qr_code.social_media_type)
    qr_code.url1 = qrformfake.url
    qr_code.save()
    return redirect(qr_code.url1)


def qrcode_social2_url_counter(request,pk):
    qr_code=Template.objects.get(id=pk)
    qr_code.social_media_type2_url_counter += 1
    qrformfake = ForFakeTemplate.objects.get(template=qr_code,social_media_type=qr_code.social_media_type2)
    qr_code.url2 = qrformfake.url
    qr_code.save()
    return redirect(qr_code.url2)

def qrcode_social3_url_counter(request,pk):
    qr_code=Template.objects.get(id=pk)
    qr_code.social_media_type3_url_counter += 1
    qrformfake = ForFakeTemplate.objects.get(template=qr_code,social_media_type=qr_code.social_media_type3)
    qr_code.url3 = qrformfake.url
    qr_code.save()
    return redirect(qr_code.url3)

def free_web_url_create(request):
    form = GenerateQRFree(request.POST or None)
    if form.is_valid():
        QR = form.save()
        qr_code = pyqrcode.create(QR.content)
        if QR.color == 'black':
            qr_color = (0, 0, 0, 255)
        elif QR.color == 'red':
            qr_color = (255, 0, 0, 255)
        elif QR.color == 'blue':
            qr_color = (0, 0, 255, 255)
        elif QR.color == 'green':
            qr_color = (0, 255, 0, 255)
        elif QR.color == 'brown':
            qr_color = (150, 75, 0, 255)
        elif QR.color == 'purple':
            qr_color = (128, 0, 128, 255)
        elif QR.color == 'pink':
            qr_color = (255, 192, 203, 255)
        elif QR.color == 'yellow':
            qr_color = (255, 255, 0, 255)
        elif QR.color == 'grey':
            qr_color = (128, 128, 128, 255)
        elif QR.color == 'light_blue':
            qr_color = (173, 216, 230, 255)
        else:
            qr_color = (0, 0, 0, 255)
        qr_code.png("{}.png".format(QR.id), scale=QR.scale, module_color=qr_color)
        copy("{}.png".format(QR.id), "static/qr_free_images/")
        os.remove("{}.png".format(QR.id))
        qrcode = QRCodeFree.objects.filter(id = QR.id).first()
        return render(request, 'free_index.html', {"qrcode": qrcode})
    return render(request, 'free_qrgenerate.html', {"form": form})


import json 
def qrcodestyle(request):
    data = {
        'color': 'black',
    }
    context = {
        'content': json.dumps(data)
    }
    return render(request, 'qr-styling.html',context=context)

