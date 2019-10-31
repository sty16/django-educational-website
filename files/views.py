from django.shortcuts import render
from django.http import HttpResponse
from .models import File
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from django.utils import timezone
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_URL = os.path.join(BASE_DIR, 'media', 'commen'),

app_name = 'files'
def index(request):
    file_list= File.objects.order_by('-upload_time')
    template = loader.get_template('files/index.html')
    context={
        "file_list" : file_list,
    }
    return HttpResponse(template.render(context,request))
    
def detail(request,file_id):
    file = get_object_or_404(File,pk=file_id)
    template = loader.get_template('files/detail.html')
    context={
        "files": files,
    }

    return HttpResponse(template.render(context,request))
def upload(request):
    if request.method == "POST":
        files = request.FILES.get("sendfile")
        os.system("mkdir uploads")
       #把文件保存到项目中一个叫做uploads的文件夹下面
        '''file_ = os.path.join("uploads", files.name)
        f = open(file_, "wb")
        for item in files.chunks():
            f.write(item)
        f.close()'''
        upload_time=timezone.localtime()
        File.objects.create(filename=files.name, username=request.user.username, description=request.POST['message'], file=files, checked='no')
    return HttpResponse('<script>alert("添加成功");location.href="/files/";</script>')


class file_show(DetailView):  # lvkai

    def get(self, request, user_name, file_name):  # lvkai add ', file_id'
        return render(request, 'file-show/file_show-main.html', {
            'mould': os.path.join(BASE_DIR, 'media', 'commen'),
            'MEDIA_URL': MEDIA_URL}
                    )

    def post(self, request):
        obj = request.FILES.get('fafafa', '1')
        print(obj.name)
        f = open(os.path.join(BASE_DIR, 'media', 'image', obj.name), 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        # return render(request, 'clashphone/test.html')
        return HttpResponse('OK')
