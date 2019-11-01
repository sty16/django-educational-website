from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Code

class CodefileForm(forms.ModelForm):
    '''用户上传文件'''
    class Meta:
        model = Code
        fields = ['userinfo','codename','desc','codefile']

