# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/20 上午9:40' 
'''
form表单
字段 <input type='text'  required>
'''

from django import forms
from django.forms import widgets
from SH1801Django.settings import SEX_CHOICES, FLAGS_CHOICES, PAY_CHOICES
from arts_app import models
from django.core.exceptions import  ValidationError

'''
会员注册表单
'''
class ArtsUserRegForm(forms.Form):
	username = forms.CharField(
		label = "用户名",
		required = True,
		min_length = 3,
		max_length = 50,
		widget = widgets.TextInput(
			attrs={
				"class":"form-control",
				"placeholder":"请输入用户名, 长度为3~50",
			}),
		error_messages = {
			"required":"对不起，用户名不能为空！",
			"min_length":"不行，长度小于3",
			"max_length":"sorry, 长度太长，大于50",
		}
	)
	password = forms.CharField(
		label="密码",
		required=True,
		min_length=6,
		max_length=20,
		widget=widgets.PasswordInput(
			attrs={
				"class": "form-control",
				"placeholder": "请输入密码, 长度为6~20",
			}),
		error_messages={
			"required": "对不起，密码不能为空！",
			"min_length": "不行，长度小于6",
			"max_length": "sorry, 长度太长，大于20",
		}
	)
	email = forms.EmailField(
		label="邮箱",
		required=True,
		widget=widgets.TextInput(
			attrs={
				"class": "form-control",
				"placeholder": "请输入邮箱",
			}),
		error_messages={
			"required": "对不起，邮箱不能为空！",
		}
	)

	def clean_username(self):
		#对username字段进行扩展校验
		username = self.cleaned_data.get("username", "")
		users = models.ArtsUser.objects.filter(username=username).count()
		if users:
			raise  ValidationError("用户已经存在！")
		return username

	def clean_email(self):
		#对email字段进行校验
		email = self.cleaned_data.get("email", "")
		users = models.ArtsUser.objects.filter(email=email).count()
		if users:
			raise  ValidationError("邮箱已经存在！")
		return email



'''
会员登录表单
'''
class ArtsUserLoginForm(forms.Form):
	username = forms.CharField(
		label="用户名",
		required=True,
		min_length=3,
		max_length=50,
		widget=widgets.TextInput(
			attrs={
				"class": "form-control",
				"placeholder": "请输入用户名, 长度为3~50",
			}),
		error_messages={
			"required": "对不起，用户名不能为空！",
			"min_length": "不行，长度小于3",
			"max_length": "sorry, 长度太长，大于50",
		}
	)
	password = forms.CharField(
		label="密码",
		required=True,
		min_length=6,
		max_length=20,
		widget=widgets.PasswordInput(
			attrs={
				"class": "form-control",
				"placeholder": "请输入密码, 长度为6~20",
			}),
		error_messages={
			"required": "对不起，密码不能为空！",
			"min_length": "不行，长度小于6",
			"max_length": "sorry, 长度太长，大于20",
		}
	)




class StudentForm(forms.Form):
	name = forms.CharField(label="学生姓名", max_length=20, required=True)
	sex = forms.ChoiceField(label="性别", choices=SEX_CHOICES)
	address = forms.CharField(label="学生地址", max_length=200)
	flag = forms.ChoiceField(label="控制字段", choices=FLAGS_CHOICES)



'''
订单表单
'''
class  OrderForms(forms.Form):
	address =  forms.CharField(
		label="配送地址",
		required=True,
		widget=widgets.TextInput(
			attrs={
				"class": "form-control",
				"placeholder": "请输入配送地址",
			}),
		error_messages={
			"required": "对不起，配送地址不能为空！",
		}
	)
	pay_type = forms.ChoiceField(
		label="支付方式",
		required=True,
		choices=PAY_CHOICES,
		widget=forms.RadioSelect()
	)
	phone = forms.CharField(
		label="手机",
		required=True,
		widget=widgets.TextInput(
			attrs={
				"class": "form-control",
				"placeholder": "请输入手机",
			}),
		error_messages={
			"required": "对不起，手机不能为空！",
		}
	)



