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

class file_show(DetailView):  # lvkai

    def get(self, request):  # lvkai add ', file_id'
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
