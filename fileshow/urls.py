from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'fileshow'
urlpatterns = [
    path(r'<user>/<file>',views.file_show, name='fileshow'),
    path(r'show',views.show, name='show')
]