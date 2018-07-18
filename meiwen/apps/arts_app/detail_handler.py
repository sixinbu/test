# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/21 上午9:43' 

from  django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from SH1801Django.utils import check_user_login

from .models import Tag, Art, Chapter
from comments.models import Comment
from comments.forms import CommentForm


'''
详情页面功能：
      接口URL：  /art/detail?id=7
      方法：GET
      输入参数说明：
          id： 文章id，（点击某一个具体的文章，传入文章id)

     输出： 渲染详情页面
'''

def DetailHandler(request):
	art_id = int(request.GET.get('id', 0))
	if art_id == 0:
		return HttpResponseRedirect('/art/index')

	art_inst = Art.objects.get(id = art_id)

	# 评论信息
	form = CommentForm()
	comment_list = Comment.objects.filter(art=art_id)

	#获取小说章节
	art_capters = Chapter.objects.filter(art=art_id)

	context = dict(
		art = art_inst,
		form = form,
		comment_list = comment_list,
		comment_count = len(comment_list),
		art_capters = art_capters,
	)

	return render(request, "home/detail_handler.html", context=context)


'''
小说章节
'''
def ArtCapterHandler(request):
	capter_id = int(request.GET.get('id', 0))
	if capter_id == 0:
		return DetailHandler(request)
	art_capter = Chapter.objects.get(id = capter_id)
	context = dict(
		art_capter = art_capter
	)
	return render(request, "home/capter_handler.html", context=context)