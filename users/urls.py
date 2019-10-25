from django.conf.urls import url
from .views import RegisterView, LoginView, VerifyView

app_name = 'users'
urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^verify/', VerifyView.as_view(), name='verify'),
]
