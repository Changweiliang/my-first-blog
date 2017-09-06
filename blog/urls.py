from django.conf.urls import url, include
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<post_id>[0-9]+)/detail/$', views.post_detail, name='post_detail')
]