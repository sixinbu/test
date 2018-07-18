# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/20 下午3:25' 

from django.shortcuts import HttpResponse, render, render_to_response, HttpResponseRedirect
from .models import Tag, Art
from SH1801Django.settings import logger
'''
接口URL：
/art/index?page=1&t=1
     Models层中类的定义也属于接口范围
     方法：GET
    输入参数说明：
       page:   第几页
       t:  标签类别，整数标识  eg: 0--全部   1--爱情小说  2—科幻小说
    输出： 渲染首页卡片式页面
'''

def IndexHandler(request):
	'''
	主页面逻辑
	:param request: 请求的url封装对象request
	:return: index_handler.html
	'''
	logger.debug("IndexHandler function enter")
	print(request.COOKIES)
	shownum = 20
	url = request.path
	t = int(request.GET.get('t', 0))
	page = int(request.GET.get('page', 1))
	tags = Tag.objects.all()
	if t == 0:
		total = Art.objects.all().count()
	else:
		total = Art.objects.filter(a_tag_id=t).count()
	context = dict(
		pagenum = 0,
		total = 0,
		prev = 1,
		next = 1,
		pagerange = range(1, 2),
		data = [],
		url = url,
		tags = tags,
		page = page,
		t = t,
	)
	logger.info(f"IndexHandler, {total}")
	if total > 0:
		import math
		pagenum = int(math.ceil(total / shownum))
		logger.warn(f"IndexHandler, pagenum: {pagenum}")
		if page < 1:
			url = url + "?page=1&t=%d" % t
			return HttpResponseRedirect(url)
		if page > pagenum:
			url = url + "?page=%d&t=%d" % (pagenum, t)
			return HttpResponseRedirect(url)
		offset = (page - 1) * shownum
		if t == 0:
			data = Art.objects.all()[offset:offset + shownum]
		else:
			data = Art.objects.filter(a_tag_id=t)[offset:offset + shownum]

		btnum = 5
		if btnum > pagenum:
			firtpage = 1
			lastpage = btnum
		else:
			if page == 1:
				firtpage = 1
				lastpage = btnum
			else:
				firtpage = page - 2
				lastpage = page + btnum - 2
				if firtpage < 1:
					firtpage = 1
				if lastpage > pagenum:
					lastpage = pagenum
		prev = page - 1
		next = page + 1
		if prev < 1:
			prev = 1
		if next > pagenum:
			next = pagenum

		context = dict(
			pagenum=pagenum,
			total=total,
			prev=prev,
			next=next,
			pagerange=range(firtpage, lastpage + 1),
			data=data,
			url=url,
			tags=tags,
			page=page,
			t=t,
		)
	logger.debug("IndexHandler function finish!")
	return  render(request, "home/index_handler.html", context=context)
