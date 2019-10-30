import os
from django.db import models
# Create your models here.


class File(models.Model):
    filename = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='upload/')
    upload_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)
    checked = models.CharField(max_length=10, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'File'
        db_table = 'File'

    def __str__(self):
        return self.title