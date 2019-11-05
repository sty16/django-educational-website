from django.conf.urls import url
from .views import CodeListView, CodeUploadView, CodeDownloadView, CodeListByDownloadView, CodeListByLikesView
app_name = "coding"

urlpatterns = [
    url(r'list/',CodeListView.as_view(),name='code_list'),
    url(r'upload/',CodeUploadView.as_view(), name='upload'),
    url(r'download/', CodeDownloadView.as_view(),name='download')
]