from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=11, verbose_name="电话", help_text="电话号码")
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