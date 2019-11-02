from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from .models import Code
from .forms import CodefileForm
from django_auth_example.settings import MEDIA_URL
from django.http import HttpResponse
import json


class CodeListView(View):

    def get(self, request):
        if request.user.is_authenticated:
            all_codes = Code.objects.all()
            return render(request, "code/code_list.html",{'all_codes':all_codes})
        else:
            all_codes = Code.objects.all()
            return render(request, "code/code_list.html",{'all_codes':all_codes})

class CodeUploadView(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            return render(request,"code/code_upload.html")
        else:
            return render(request,"login.html")

    def post(self, request):
        codefile_form = CodefileForm(request.POST, request.FILES)
        if codefile_form.is_valid():
            file_obj = request.FILES.get('codefile','') #获取上传文件
            codefile = Code()
            codefile.userinfo = codefile_form.cleaned_data['userinfo']
            codefile.codename = codefile_form.cleaned_data['codename']
            codefile.desc = codefile_form.cleaned_data['desc']
            codefile.codefile = codefile_form.cleaned_data['codefile']
            # TODO 后台语法自动检测文件
            codefile.save()
            all_codes = Code.objects.all()
            return render(request, "code/code_list.html", {'all_codes':all_codes})
        else:
            pass 

class CodeDownloadView(View):
    def get(self,request):
        pass
    def post(self,request):
        data = {'status':'failure','msg': '下载失败','FilePath':''}
        file_id = request.POST.get("File_id","")
        file_id = int(file_id)
        code_file = Code.objects.get(pk=file_id)
        num = code_file.download_nums
        code_file.download_nums = num + 1
        code_file.save()
        if code_file:
            data["status"] = 'success'
            data["FilePath"] = str(code_file.codefile)
            data["msg"] = '下载成功'
            data = json.dumps(data)
            response =  HttpResponse(data,content_type="application/json")
            return response
        else:
            data = json.dumps(data)
            return HttpResponse(data,content_type="application/json")


