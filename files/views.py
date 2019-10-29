from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from django.template import loader
from django.shortcuts import get_object_or_404, render
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def index(request):
    file_list= File.objects.order_by('-create_time')
    template = loader.get_template('file/index.html')
    context={
        "file_list" : file_list,
    }
    return HttpResponse(template.render(context,request))