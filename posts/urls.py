from django.conf.urls import include,url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', "posts.views.posts_list"),
    url(r'^create/$', "posts.views.posts_create"),
    url(r'^(?P<id>\d+)/$', "posts.views.posts_detail"),
    url(r'^update/$', "posts.views.posts_update"),
    url(r'^delete/$', "posts.views.posts_delete"),
    # url(r'^abc/$', "posts.views.posts_home"),
]