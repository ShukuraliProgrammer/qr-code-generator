import random
from .forms import TemplateForm, UserForm
from django.shortcuts import redirect, render
from .models import QrCode, Template
from django.db.models import Count
import qrcode
from django.core.files import File
from io import BytesIO
from PIL import Image, ImageDraw
from django.contrib.auth import authenticate, login

def qrcodes_list(request):
    qr_code=QrCode.objects.all().order_by('-created_at')
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
        print("user is auth")
        return  redirect('template-list')
    else:
        print("Coming request")
        if request.method == 'POST':
            print("came request",request.POST)
            email = request.POST['email']
            password = request.POST['password']
            
            user = authenticate(username=email, password=password)
            print("this is user",user)
            if user is not None:
                print("user is not none")
                login(request, user)
                return redirect('template-list')
            else:
                messages.info(request, 'Invalid Username or Password')
                return redirect('login_user')
        else:
            return render(request, 'login.html')

def qr_template_list(request):
    
    return render(request,"tmp_list.html")
    # else:
    #     qr_code=QrCode.objects.all().order_by('-created_at')
    #     return render(request,'qrcodes-list.html',{'qr_code':qr_code})

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
            form.instance.image = request.FILES.get('image')
            form.save()
            qrcode_img = qrcode.make('10.10.1.89:8000/phone-detail/{}'.format(form.instance.id))
            canvas=Image.new("RGB", (900,900),"white")
            draw=ImageDraw.Draw(canvas)
            canvas.paste(qrcode_img)
            buffer=BytesIO()
            canvas.save(buffer,"PNG")
            form.instance.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
            canvas.close()
            obj1 = QrCode()
            obj1.image.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
            obj1.url = f'/phone-detail/{form.instance.id}'
            obj1.save()
            canvas.close()
            return redirect('qrcodes-list')
        return redirect('template-list')
    context = {
        'form':TemplateForm()
    }
    return render(request,"tmp_social.html",context=context)

def phoneDetailViews(request,pk):
    qr_code=Template.objects.get(id=pk)

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


