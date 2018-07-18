# -*- coding: utf-8 -*-

__author__ = 'zhougy'
__date__ = '202018/6/19 下午2:00' 

from django.conf.urls import url
from .views import hello_world, index, test, stu_forms, query_stu, add
from .index_handler import IndexHandler
from .search_handler import SearchHandler
from .detail_handler import DetailHandler, ArtCapterHandler
from arts_app import user_manage
from arts_app import cart_handler

'''
二级路由入口文件
'''

urlpatterns = [
	url(r'^hello/$', hello_world),
	url(r'^test_index/$', index),
	url(r'^test/$', test),
	url(r'^stu_forms/$', stu_forms),
	url(r'^query_stu/$', query_stu),
	url(r'^add/$', add),
	url(r'^index/$', IndexHandler),
	url(r'^search/$', SearchHandler),
	url(r'^detail/$', DetailHandler),
	url(r'^register/$', user_manage.RegisterHandler, name="user_register"),
	url(r'^login/$', user_manage.LoginHandler, name="user_login"),
	url(r'^logout/$', user_manage.LogoutHandler, name="user_logout"),
	url(r'^cart/view/$', cart_handler.ViewCartHandler),
	url(r'^cart/add/$', cart_handler.AddCartHandler),
    url(r'^cart/clean/$', cart_handler.CleanCartHandler),
	url(r'^cart/order/$', cart_handler.CartOrderHandler),
	url(r'^capter/$', ArtCapterHandler),
]