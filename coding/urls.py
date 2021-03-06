from django.conf.urls import url
from .views import CodeListView, CodeUploadView, CodeDownloadView,CodeListByTimeView, CodeListByDownloadView, CodeListByLikesView
from .views import CodeFavnumView, CodeCheckView
app_name = "coding"

urlpatterns = [
    url(r'list/',CodeListView.as_view(),name='code_list'),
    url(r'upload/',CodeUploadView.as_view(), name='upload'),
    url(r'download/', CodeDownloadView.as_view(),name='download'),
    url(r'sort_bytime',CodeListByTimeView.as_view(),name="sort_bytime"),
    url(r'sort_bydownload',CodeListByDownloadView.as_view(),name="sort_bydownload"),
    url(r'sort_bylikes',CodeListByLikesView.as_view(),name="sort_bylikes"),
    url(r'fav_num/',CodeFavnumView.as_view(),name="fav_num"),
    url(r'code_check/',CodeCheckView.as_view(),name='code_check')
]