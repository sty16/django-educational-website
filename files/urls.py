from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'files'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:file_id>/',views.detail, name='detail'),
]