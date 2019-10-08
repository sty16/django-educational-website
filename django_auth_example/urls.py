"""django_auth_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
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
    url(r'^$', views.index, name='index')
]
