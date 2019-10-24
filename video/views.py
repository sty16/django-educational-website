from django.http import HttpResponse
from .models import Video
from django.template import loader
from django.shortcuts import get_object_or_404, render
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Create your views here.
def index(request):
    video_list= Video.objects.order_by('-create_time')
    template = loader.get_template('video/index.html')
    context={
        "video_list" : video_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request,video_id):
    video = get_object_or_404(Video,pk=video_id)
    template = loader.get_template('video/detail.html')
    context={
        "video": video,
        "upload_files_dir" : os.path.join(BASE_DIR, "uploads"),
    }
    return HttpResponse(template.render(context,request))
