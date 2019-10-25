from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'video'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:video_id>/',views.detail, name='detail'),
]

