from django.contrib.auth.forms import UserCreationForm
from django import forms
from captcha.fields import CaptchaField
from .models import User


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # 验证码
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
