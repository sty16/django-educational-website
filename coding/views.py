from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from .models import Code
from .forms import CodefileForm
from django_auth_example.settings import MEDIA_URL
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
import json
import os

Base_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
File_DIR  = os.path.join(Base_DIR,"media","codefile")
class CodeListView(View):

    def get(self, request):
        if request.user.is_authenticated:
            all_codes = Code.objects.filter(syntax_check=True) # TODO filter 条件
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
                return render(request, "code/code_list.html", {'all_codes':all_codes})
            else:
                codefile.delete()
                os.popen('del '+file_url+'\n') # 如果是linux，这里改成 os.popen('rm '+fileurl+'\n')
                error_info = os.popen('pyflakes ' + file_url, 'r' , 1).read()
                data = {"status":"failure"}
                data["error_info"] = error_info
                data = json.dumps(data)
                return HttpResponse(data, content_type="application/json")


            # checkresult = os.popen('pyflakes '+ fileurl +'\n').read()
            # print("\n\n\n\n\n\n"+fileurl+"\n"+checkresult+"\n\n\n\n\n")
            # if len(checkresult) == 0: # 如果检查结果无误，则没有返回值
            #     codefile.syntax_check = True
            #     return render(request, "code/code_list.html", {'all_codes':all_codes})
            # else:
            #     os.popen('del '+fileurl+'\n') # 如果是linux，这里改成 os.popen('rm '+fileurl+'\n')
            #     codefile.delete()   # 从数据库中删除
            #     data = {"status":"failure"}
                # return HttpResponse(data, content_type="application/json")


class CodeDownloadView(View):
    def get(self,request):
        pass
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
            response = FileResponse(download_file)
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


