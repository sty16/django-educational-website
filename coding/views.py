from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from .models import Code, LikeRecord
from .forms import CodefileForm
from django_auth_example.settings import MEDIA_URL
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import json
import os

Base_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
File_DIR  = os.path.join(Base_DIR,"media","codefile")
class CodeListView(View):

    def get(self, request):
        if request.user.is_authenticated:
            codes = Code.objects.filter(star_check=True).order_by("add_time") # TODO filter 条件
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(codes , 9)
            all_codes = p.page(page)
            return render(request, "code/code_list.html", {'all_codes':all_codes, 'content_type':'code_list'})
        else:
            return render(request,"login.html")

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
            codefile.save()
            # TODO 后台语法自动检测文件
            all_codes = Code.objects.all()
            filename = str(codefile.codefile)
            filename = filename.split('/')[1]
            file_url = os.path.join(File_DIR, filename)
            check_result = os.system('pyflakes ' + file_url)
            print(type(check_result))
            if  check_result == 0:
                codefile.syntax_check = True
                codefile.save()
                # return render(request, "code/code_list.html", {'all_codes':all_codes})
                user_name = request.user.username
                unchecked_codes=Code.objects.filter(userinfo=user_name, manual_check=0)
                data = {"status":"success"}
                data = json.dumps(data)
                return HttpResponse(data, content_type="application/json")
            else:
                codefile.delete()
                # os.popen('del '+file_url+'\n') # 如果是linux，这里改成 os.popen('rm '+fileurl+'\n')
                # error_info = os.popen('pyflakes ' + file_url, 'r' , 1).read()
                data = {"status":"wrong"}
                # data["error_info"] = error_info
                data = json.dumps(data)
                return HttpResponse(data, content_type="application/json")


class CodeDownloadView(View):
    def get(self,request):
        data = {'status':'failure',"filename":""}
        file_id = request.GET.get("file_id","")
        file_id = int(file_id)
        code_file = Code.objects.get(pk=file_id)
        if code_file:
            filepath = str(code_file.codefile)
            filename = filepath.split('/')[1]
            data["status"] = "success"
            data["filename"] = filename
            data = json.dumps(data)
            print('eeeeeeeeeeeeeeeee')
            return HttpResponse(data, content_type="application/json")
        else:
            return HttpResponse(data, content_type="application/json")
    def post(self,request):
        data = {'status':'failure','msg': '下载失败','FilePath':''}
        file_id = request.POST.get("File_id","")
        file_id = int(file_id)
        code_file = Code.objects.get(pk=file_id)
        if code_file:
            num = code_file.download_nums
            code_file.download_nums = num + 1
            code_file.save()
            filepath = str(code_file.codefile)
            filename = filepath.split('/')[1]
            filepath = os.path.join(File_DIR,filename)
            download_file = open(filepath,'rb')
            response = StreamingHttpResponse(download_file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
            return response
        else:
            data = json.dumps(data)
            return HttpResponse(data,content_type="application/json")

            # data["status"] = 'success'
            # data["FilePath"] = str(code_file.codefile)
            # data["msg"] = '下载成功'
            # data = json.dumps(data)
            # response =  HttpResponse(data,content_type="application/json")
            # return response

class CodeListByTimeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            codes = Code.objects.filter(star_check=True).order_by("-add_time") # TODO filter 条件
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(codes , 9)
            all_codes = p.page(page)
            return render(request, "code/code_list.html", {'all_codes':all_codes, 'content_type':'time_list'})
        else:
             return render(request,"login.html")


class CodeListByDownloadView(View):
    def get(self, request):
        if request.user.is_authenticated:
            codes = Code.objects.filter(star_check=True).order_by("-download_nums") # TODO filter 条件syntax_check
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(codes , 9)
            all_codes = p.page(page)
            return render(request, "code/code_list.html", {'all_codes':all_codes, 'content_type':'download_list'})
        else:
             return render(request,"login.html")


class CodeListByLikesView(View):
    def get(self, request):
        if request.user.is_authenticated:
            codes = Code.objects.filter(star_check=True).order_by("-fav_nums") # TODO filter 条件 syntax_check
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(codes , 9)
            all_codes = p.page(page)
            return render(request, "code/code_list.html", {'all_codes':all_codes,'content_type':'fav_list'})
        else:
             return render(request,"login.html")

class CodeFavnumView(View):
    def get(self,request):
        pass

    def post(self,request):
        data = {"status":"failure"}
        file_id = request.POST.get("file_id","")
        user_name = request.user.username
        codefile = Code.objects.get(pk=int(file_id))
        Like_record = LikeRecord.objects.filter(Like_user=user_name).filter(Like_codefile=codefile)
        print(len(Like_record))
        if Like_record:
            data = json.dumps(data)
            return HttpResponse(data, content_type="application/json")
        else:
            like_newrecord = LikeRecord(Like_user=user_name)
            like_newrecord.Like_codefile = codefile
            like_newrecord.save()
            codefile.fav_nums = codefile.fav_nums + 1
            codefile.save()
            data["status"] = "success"
            data = json.dumps(data)
            return HttpResponse(data,content_type="application/json")

class CodeCheckView(View):
 
    def get(self, request):
        if request.user.is_authenticated:
            codes = Code.objects.filter(manual_check=False).order_by("-add_time") # TODO filter 条件
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(codes , 9)
            all_codes = p.page(page)
            return render(request, "code/code_check.html", {'all_codes':all_codes, 'content_type':'code_check'})
        else:
            return render(request,"login.html")
    def post(self, request):
        data = {'status':'failure'}
        file_id = request.POST.get("File_id","")
        status = request.POST.get("result","")
        file_id = int(file_id)
        code_file = Code.objects.get(pk=file_id)
        if code_file:
            code_file.manual_check = True
            if status == "True":
                code_file.result_check = True
            code_file.save()
            data['status'] = "success"
            data = json.dumps(data)
            response = HttpResponse(data)
            return response
        else:
            data = json.dumps(data)
            return HttpResponse(data,content_type="application/json")

