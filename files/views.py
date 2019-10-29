from django.shortcuts import render
from django.http import HttpResponse
from .models import File
from django.template import loader
from django.shortcuts import get_object_or_404, render
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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
