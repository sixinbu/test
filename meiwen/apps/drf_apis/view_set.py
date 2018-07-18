# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/7/7 上午10:43' 

'''
采用视图集和路由器实现
'''
from rest_framework import viewsets
from rest_framework import permissions

from arts_app.models import ArtsUser, Tag, Art, Chapter, ProductOrder, LineItem
from comments.models import Comment

from drf_apis  import serializers
from drf_apis.permissions import IsOwnerOrReadOnly


class ArtsUserViewSet(viewsets.ModelViewSet):
	queryset = ArtsUser.objects.all()
	serializer_class = serializers.ArtsUserSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = serializers.TagSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ArtViewSet(viewsets.ModelViewSet):
	queryset = Art.objects.all()
	serializer_class = serializers.ArtSerializer

	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)



class ChapterViewSet(viewsets.ModelViewSet):
	queryset = Chapter.objects.all()
	serializer_class = serializers.ChapterSerializer

	permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)




class ProductOrderViewSet(viewsets.ModelViewSet):
	queryset = ProductOrder.objects.all()
	serializer_class = serializers.ProductOrderSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class LineItemViewSet(viewsets.ModelViewSet):
	queryset = LineItem.objects.all()
	serializer_class = serializers.LineItemSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)




class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = serializers.CommentSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


