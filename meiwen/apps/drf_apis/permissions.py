# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/7/2 下午8:13' 

#权限管理
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	'''
	自定义权限功能，只允许对象的所有者编辑它
	'''
	def  has_object_permission(self, request, view, obj):
		#
		if request.method in permissions.SAFE_METHODS:
			return True

		#只有所有者才具有写权限，其他只能有读权限
		return  obj.operator == request.user




