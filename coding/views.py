from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from .models import Code

class CodeListView(View):

    def get(self, request):
        all_codes = Code.objects.all()
        return render(request, "code/code_list.html",{'all_codes':all_codes})

class CodeUploadView(View):
    
    def get(self, request):
        return render(request,"code/code_upload.html")
