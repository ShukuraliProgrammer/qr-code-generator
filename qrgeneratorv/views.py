from multiprocessing import context
from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import redirect, render
from .models import QrCode
from django.db.models import Count
def home(request):
    context={}
    if request.method == "POST":
        Url=request.POST['url']
        print(f"Url - qr code----> {Url}")
        if QrCode.objects.filter(url=Url):
            context = {'message':'Bu url generatsiya qilingan.'}
            return render(request,"home.html",context)
        else:
            qr_obj = QrCode.objects.create(url=Url)
            qr_obj.save()
        
        return redirect('QrCode')
    return render(request,"home.html",context=context)

def qr_code(request):

    qr_code=QrCode.objects.all().order_by('-created_at')

    return render(request,"qrcodes-list.html",{'qr_code':qr_code})

def qr_url(request,pk):
    qr_code=QrCode.objects.get(id=pk)
    qr_code.url_counter += 1
    qr_code.save()
    
    return redirect(qr_code.url)

def qrcode_detailView(request,pk):
    qr_code=QrCode.objects.get(id=pk)
    return render(request,"qrcode-detail.html",{'qr':qr_code})
