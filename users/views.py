# coding=utf-8
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from .forms import VerifyForm
from django.views.generic import View
from .models import User, EmailVerifyRecord
from .models import MobileVerify
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_email
from django.contrib.auth import authenticate,login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from utils.aliyun import send_code
from datetime import datetime, timedelta



class RegisterView(View):
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username',None)
            if User.objects.filter(username = user_name):
                return render(request, 'register_email.html', {'register_form': register_form, 'msg': '用户名已存在'})
            user_email = request.POST.get('email', None)
            # 如果用户已存在，则提示错误信息
            if User.objects.filter(email = user_email):
                return render(request, 'register_email.html', {'register_form':register_form,'msg': '邮箱已存在'})
            pass_word = request.POST.get('password', None)
            # 实例化一个user_profile对象
            user_profile = User()
            user_profile.username = user_name
            user_profile.email = user_email
            user_profile.is_active = False
            # 对保存到数据库的密码加密
            user_profile.password = make_password(pass_word)
            user_profile.save()
            status = send_register_email(user_email, 'register')
            if status:
                return render(request, 'send_success.html')
            else:
                return render(request, 'active_fail.html')
        else:
            return render(request,'register_email.html',{'register_form':register_form})


    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register_email.html', context={'register_form':register_form})

class VerifyView(View):
    def post(self, request):
        verify_form = VerifyForm(request.POST)
        if verify_form.is_valid():
            user_name = request.POST.get('username',None)
            user_mobile = request.POST.get('mobile', None)
            pass_word = request.POST.get('password', None)
            if not verify_form.cleaned_data['send']:
                # 实例化一个user_profile对象,未发送验证码时候的处理
                user_profile = User()
                user_profile.username = user_name
                user_profile.mobile = user_mobile
                user_profile.is_active = False
                user_profile.password = make_password(pass_word)
                sms_status = send_code(user_mobile)
                if (eval(sms_status)["Message"]) == 'OK':
                    user_profile.save()
                    verify_form.cleaned_data['send'] = True
                    verify_form = VerifyForm(initial=verify_form.cleaned_data)
                    return render(request, 'register.html', {'verify_form':verify_form,'msg': '已发送，请注意查收'})
                else:
                    return render(request, 'register.html', {'verify_form':verify_form,'msg': '请重新发送验证码'})
            else:
                # 发送验证码
                code = request.POST.get('mobile_code', None)
                verify_records = MobileVerify.objects.filter(mobile=user_mobile).order_by("-send_time")
                if verify_records:
                    last_record = verify_records[0]
                    # TODO can't compare offset-naive and offset-aware datetimes
                    # 有效期为五分钟
                    # five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
                    # if five_mintes_ago > last_record.send_time:
                    #     return render(request, 'register.html', {'verify_form':verify_form,'msg': '过期，请重新发送'})
                    if last_record.code != code:
                        return render(request, 'register.html', {'verify_form':verify_form,'msg': '验证码错误'})
                    else:
                        user = User.objects.get(mobile=user_mobile,username=user_name)
                        if user:
                            user.is_active = True
                            user.save()
                        return render(request, 'register.html', {'verify_form':verify_form,'msg': '注册成功'})
        else:
            return render(request,'register.html',{'verify_form':verify_form})

    def get(self, request):
        verify_form = VerifyForm()
        return render(request, 'register.html', context={'verify_form':verify_form})


class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code = active_code)

        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 查找到邮箱对应的user
                user = User.objects.get(email=email)
                user.is_active = True
                user.save()
         # 验证码不对的时候跳转到激活失败页面
        else:
            return render(request, 'active_fail.html')
        # 激活成功跳转到登录页面
        return render(request, "login.html", )




class LoginView(View):
    '''用户登录'''

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取用户提交的用户名和密码
            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)
            # 成功返回user对象,失败None
            user = authenticate(username=user_name, password=pass_word)
            # 如果不是null说明验证成功
            if user is not None:
                if user.is_active:
                    # 只有注册激活才能登录
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
            # 只有当用户名或密码不存在时，才返回错误信息到前端
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误','login_form':login_form})

        # form.is_valid（）已经判断不合法了，所以这里不需要再返回错误信息到前端了
        else:
            return render(request,'login.html',{'login_form':login_form})

def index(request):
    return render(request, 'satellite_index.html')
