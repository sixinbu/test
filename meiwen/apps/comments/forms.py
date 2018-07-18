# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/28 下午2:30' 

from django import forms
from comments.models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'title', 'text']




