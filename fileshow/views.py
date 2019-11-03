from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from django.utils import timezone
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_URL = os.path.join(BASE_DIR, 'media', 'commen'),
# Create your views here.
def file_show(request, user_name, file_name):
    return render(request, 'file-show/file_show-main.html',{text:'12345'})