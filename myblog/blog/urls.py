from django.conf.urls import url, handler404, handler500
from blog import views

app_name = 'blog'


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'post/all/$', views.PostView.as_view(), name='post'),
    url(r'post/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'post/category/(?P<pk>\d+)/$', views.CategoryView.as_view(), name='category'),
    url(r'post/tag/(?P<pk>\d+)/$', views.TagView.as_view(), name='tag'),

]

handler404 = views.page_not_found
handler500 = views.page_error
