"""SH1801Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
#from django.contrib import admin
import xadmin

# url_path = "/static/" + urljoin(USettings.gSettings.MEDIA_URL, OutputPathFormat)

'''
工程项目一级路由文件
'''
urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^art/', include("arts_app.urls")),
    url(r'^message/', include("message.urls")),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^statistic/', include("statistic.urls")),
    url(r'^comments/', include("comments.urls")),
    url(r'^apis/', include("drf_apis.urls")),
]


