from django.db import models
from datetime import datetime 


# Create your models here.
class Code(models.Model):
    userinfo= models.CharField("上传用户",max_length=150,blank=True)
    codename = models.CharField("程序名",max_length=50,blank=True)
    desc = models.CharField("程序描述",max_length=300,blank=True)
    fav_nums = models.IntegerField("点赞人数",default=0,blank=True)
    download_nums = models.IntegerField("下载数",default=0,blank=True)
    add_time = models.DateTimeField("添加时间",default=datetime.now,blank=True)
    syntax_check = models.BooleanField("语法审核", default=False,blank=True)
    manual_check = models.BooleanField("人工审核",default=False,blank=True)
    result_check = models.BooleanField("人工审核结果",default=False, blank=True)
    star_check = models.BooleanField("是否上星", default=False, blank=True)
    codefile = models.FileField(upload_to="codefile/",blank=True)

    class Meta:
        verbose_name = "上传代码列表"
        verbose_name_plural = verbose_name

class LikeRecord(models.Model):
    Like_user = models.CharField("点赞用户",max_length=150,blank=True)
    Like_time = models.DateTimeField("点赞时间",default=datetime.now,blank=True)
    Like_codefile = models.ForeignKey(Code, related_name="Code",on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name = "点赞列表"
        verbose_name_plural = verbose_name
