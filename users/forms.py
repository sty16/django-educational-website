from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField
from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,initial='')
    email = forms.EmailField(required=True,initial='')
    password = forms.CharField(required=True, min_length=5,initial='')
    # 验证码
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

class VerifyForm(forms.Form):
    username = forms.CharField(required=True,initial='')
    mobile = forms.CharField(required=True,initial='')
    password = forms.CharField(required=True,initial='')
    send = forms.BooleanField(required=False, initial=False)
    code = forms.CharField(required=False,initial='')
    
    class Meta(UserCreationForm.Meta):
        model = User

class UploadImageForm(forms.ModelForm):
    '''用户更改图像'''
    class Meta:
        model = User
        fields = ['image']
