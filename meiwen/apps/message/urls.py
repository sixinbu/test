# -*- coding: utf-8 -*-

__author__ = 'zhougy'
__date__ = '202018/6/19 下午2:00'

from django.conf.urls import url
from .views import say_hello, MessageSubmitHandler, MessageSubmitHandlerV2

'''
二级路由入口文件
'''

urlpatterns = [
	url(r'^$', MessageSubmitHandler, name="msg_form"),  #msg_form 代替  /message/
	url(r'^v2$', MessageSubmitHandlerV2, name="msg_form_v2"),
	url(r'^say_hello/$', say_hello, name="say_hi"),
]
