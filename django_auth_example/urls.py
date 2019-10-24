from django.conf.urls import url, include
from django.contrib import admin
from users import views
from users.views import ActiveUserView
import xadmin
from xadmin.plugins import xversion
from django.urls import path,re_path
xadmin.autodiscover()
xversion.register_models()


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 别忘记在顶部引入 include 函数
    url(r'^xadmin/',xadmin.site.urls, name='xadmin'), # 添加管理员登录
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('video/', include('video.urls')),
    url(r'^$', views.index, name='index')
]
