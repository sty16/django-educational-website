import os
from django.db import models
# Create your models here.


class File(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='file/')
    create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)

    class Meta:
        verbose_name_plural = 'File'
        db_table = 'File'

    def __str__(self):
        return self.title