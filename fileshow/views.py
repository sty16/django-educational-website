from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from django.utils import timezone
import os
import sys
sys.path.append("..")

from coding.models import Code


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_URL_BASE = str(os.path.join(BASE_DIR, 'media', 'codefile')),
# Create your views here.
#def file_show(request, user, file):

def file_show(request,user,file):
    template = loader.get_template('file-show/file_show-main.html')
    file_id = int(file)
    code_file = Code.objects.get(pk=file_id)
    filename = str(code_file.codefile).split('/')[1]
    print(type(FILE_URL_BASE), type(filename))
    fileurl = FILE_URL_BASE[0]+'\\'+filename
    with open(fileurl) as file_obj:
        contents = file_obj.read()
    context={'text':contents,}
    return HttpResponse(template.render(context,request))


def show(self, request):
    obj = request.FILES.get('fafafa', '1')
    print(obj.name)
    f = open(os.path.join(BASE_DIR, 'media', 'image', obj.name), 'wb')
    for chunk in obj.chunks():
        f.write(chunk)
    f.close()
    # return render(request, 'clashphone/test.html')
    return HttpResponse('OK')
'''class file_show(DetailView):  # lvkai
    def get(self, request):  # lvkai add ', file_id'
        return render(request, 'file-show/file_show-main.html', {'mould': os.path.join(BASE_DIR, 'media', 'commen'),'MEDIA_URL': MEDIA_URL,'text':'12345'},)

    def post(self, request):
        obj = request.FILES.get('fafafa', '1')
        print(obj.name)
        f = open(os.path.join(BASE_DIR, 'media', 'image', obj.name), 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        # return render(request, 'clashphone/test.html')
        return HttpResponse('OK')'''