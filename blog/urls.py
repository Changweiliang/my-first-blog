from django.conf.urls import url, include
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.PostDetail.as_view(), name='post_detail')
]