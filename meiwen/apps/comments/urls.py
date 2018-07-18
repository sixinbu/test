# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/28 下午3:57' 

from django.conf.urls import url
from comments import views

app_name = 'comments'
urlpatterns = [
    url(r'^art/(?P<art_pk>[0-9]+)/$', views.art_comment, name='art_comment'),
]
