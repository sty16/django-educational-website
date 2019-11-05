from django.conf.urls import url
from .views import RegisterView, LoginView, VerifyView, LogoutView, UserinfoView,UsercodeView
from .views import UploadImageView, UpdatePwdView, SendEmailCodeView, SendMobileCodeView
from .views import UpdateEmailView, UpdateMobileView, UpdateUserinfoView, UpdatePwdSendView


app_name = 'users'
urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^verify/', VerifyView.as_view(), name='verify'),
    url(r'^logout/',LogoutView.as_view(),name='logout'),
    url(r'^info/',UserinfoView.as_view(),name='user_info'),
    url(r'^image/upload/', UploadImageView.as_view(),name='image_upload'),
    url(r'update/pwd/',UpdatePwdView.as_view(),name='update_pwd'),
    url(r'update/send_emailcode/', SendEmailCodeView.as_view(), name='send_emailcode'),
    url(r'update/send_mobilecode/', SendMobileCodeView.as_view(),name='send_mobilecode'),
    url(r'update_email/', UpdateEmailView.as_view(),name='update_email'),
    url(r'update_mobile/', UpdateMobileView.as_view(),name='update_mobile'),
    url(r'update_userinfo/',UpdateUserinfoView.as_view(),name="update_userinfo"),
    url(r'update/pwd_send/',UpdatePwdSendView.as_view(),name="update_pwdsend"),
    url(r'^mycode/',UsercodeView.as_view(),name='user_code')
]
