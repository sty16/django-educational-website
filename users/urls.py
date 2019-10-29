from django.conf.urls import url
from .views import RegisterView, LoginView, VerifyView, LogoutView, UserinfoView
from .views import UploadImageView, UpdatePwdView


app_name = 'users'
urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^verify/', VerifyView.as_view(), name='verify'),
    url(r'^logout/',LogoutView.as_view(),name='logout'),
    url(r'^info/',UserinfoView.as_view(),name='user_info'),
    url(r'^image/upload/', UploadImageView.as_view(),name='image_upload'),
    url(r'update/pwd/',UpdatePwdView.as_view(),name='update_pwd'),
]
