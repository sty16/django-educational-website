from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField
from .models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 验证码
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)

class VerifyForm(forms.Form):
    username = forms.CharField(required=True)
    mobile = forms.CharField(required=False)
    password = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User


