# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/23 上午9:46' 

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from arts_app import forms
from arts_app import models

from django.views.decorators.csrf import csrf_exempt
from SH1801Django import utils

def create_pwd_md5(str_pwd):
	import hashlib
	h1 = hashlib.md5()
	h1.update(str_pwd.encode(encoding="utf-8"))
	return h1.hexdigest()


'''
用户注册功能
'''
@csrf_exempt
def RegisterHandler(request):
	userform = forms.ArtsUserRegForm()
	if request.method == "POST":
		userform = forms.ArtsUserRegForm(data=request.POST)
		if not userform.is_valid():
			utils.flash(request, "error", f"用户注册失败")
			context = dict(
				form=forms.ArtsUserRegForm(data=request.POST)
			)
			return render(request, "home/register_handler.html", context=context)

		username = userform.cleaned_data['username']
		password = create_pwd_md5(userform.cleaned_data['password'])
		email = userform.cleaned_data['email']
		art_user = models.ArtsUser(username=username, password=password, email=email)
		art_user.save()
		#return HttpResponse(f"恭喜, 注册用户{username}成功！")
		utils.flash(request, "success", f"恭喜, 注册用户{username}成功！")

	context = dict(
		form = userform
	)
	return render(request, "home/register_handler.html", context=context)


'''
会员登录功能
'''
@csrf_exempt
def LoginHandler(request):
	userform = forms.ArtsUserLoginForm()
	if request.method == "POST":
		userform = forms.ArtsUserLoginForm(data=request.POST)
		if not userform.is_valid():
			utils.flash(request, "error", f"用户登录失败")
			context = dict(form=userform)
			return render(request, "home/login_handler.html", context=context)
		username = userform.cleaned_data['username']
		password = create_pwd_md5(userform.cleaned_data['password'])
		user = models.ArtsUser.objects.filter(username__exact=username,
											  password__exact=password).first()
		if user:
			#store the user into session key:muser
			request.session['muser'] = user
			return HttpResponseRedirect("/art/index")
		else:
			#return HttpResponse(f"用户{username}登录失败")
			utils.flash(request, "error", f"用户{username}登录失败")

	context = dict(form=userform)
	return render(request, "home/login_handler.html", context=context)



def LogoutHandler(request):
	del request.session['muser']
	return HttpResponseRedirect("/art/login")