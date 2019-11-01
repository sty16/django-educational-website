from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from .models import Code
from .forms import CodefileForm


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
            return render(request, "code/code_list.html",{'all_codes':all_codes})
        pass 
