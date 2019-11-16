from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    gender_choices = (
        ('male','男'),
        ('female','女')
    )
    is_admin = models.BooleanField('管理员',blank=True, default=False)
    nickname = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=11,blank=True, verbose_name="电话", help_text="电话号码")
    birthday = models.CharField('生日',null=True,blank=True, max_length=100)
    gender = models.CharField('性别',max_length=10,blank=True,choices=gender_choices,default='male')
    address = models.CharField('地址',blank=True,max_length=100,default='')
    image = models.ImageField(upload_to='user_image/',blank=True,default='user_image/default.png',max_length=100)
    class Meta(AbstractUser.Meta):
        pass

class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码'),
        ('update_email','修改邮箱')
    )

    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=30)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
        
class MobileVerify(models.Model):
    code = models.CharField('验证码', max_length=10)
    mobile = models.CharField(max_length=11, verbose_name="电话", help_text="电话号码")
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '手机验证码'
        verbose_name_plural = verbose_name

