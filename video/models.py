import os
from django.db import models
# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='vedio/')
    create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = '视频'
        db_table = 'Video'

    def __str__(self):
        return self.title