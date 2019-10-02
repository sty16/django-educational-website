from django.conf.urls import url
from .views import RegisterView

app_name = 'users'
urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name='register'),

]
