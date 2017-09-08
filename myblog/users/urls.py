from django.conf.urls import url, include
from users import views
app_name = 'users'


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^account/$', views.user_detail, name='user_detail'),


]