from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^2', views.post_list2, name='post_list2'),
    url(r'^3', views.post_list3, name='post_list3'),
    url(r'^post/(?P<pk>\d+)', views.post_detail, name="post_detail"),
    url(r'^post/new/$', views.post_new, name="post_new"),
]
