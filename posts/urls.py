from django.conf.urls import include,url
from django.contrib import admin

# from . import views

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

# urlpatterns = [
#     url(r'^$', "posts.views.posts_list"),
#     url(r'^create/$', "posts.views.posts_create"),
#     url(r'^(?P<id>\d+)/$', "posts.views.posts_detail", name="detail"),
#     url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
#     url(r'^delete/$', "posts.views.posts_delete"),
#     # url(r'^abc/$', "posts.views.posts_home"),
# ]
urlpatterns = [
	url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]