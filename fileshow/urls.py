from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'fileshow'
urlpatterns = [
    path('coding/list/<str:user_name>/<str:file_name>',views.file_show, name='file_show'),
]