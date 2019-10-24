from django.conf.urls import url
from . import views

app_name = 'video'
urlpatterns = [
    url(r'^index',views.index, name='index'),
    url('<int:video_id>/',views.detail, name='detail'),
]

