from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'fileshow'
urlpatterns = [
    path('',views.index, name='index'),
    path('coding/<str:user_name>/<str:file_name>',views.file_show.as_view(), name='file_show'),
    path('upload/',views.upload, name='file_upload'),
]