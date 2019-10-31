from django.conf.urls import url
from .views import CodeListView, CodeUploadView
app_name = "coding"

urlpatterns = [
    url(r'list/',CodeListView.as_view(),name='code_list'),
    url(r'upload/',CodeUploadView.as_view(), name='upload')
]