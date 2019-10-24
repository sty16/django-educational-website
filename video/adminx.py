import xadmin
from django.contrib import admin
from .models import Video

class VideoAdmin(object):
    list_display = ['title', 'description', 'file','create_time']
    search_fields = ['title', 'description', 'file','create_time']
    list_filter = ['title', 'description', 'file','create_time']

# admin.site.unregister(User)
xadmin.site.register(Video, VideoAdmin)