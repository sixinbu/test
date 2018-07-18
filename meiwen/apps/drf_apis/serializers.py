# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '202018/6/21 下午9:47' 

from rest_framework import serializers
from arts_app.models import ArtsUser, Tag, Art, Chapter, ProductOrder, LineItem
from comments.models import Comment


class ArtsUserSerializer(serializers.ModelSerializer):
	#operator = serializers.ReadOnlyField(source="operator.username")

	#mongod - -dbpath E:\mongodb\3rd - party\mongodb\bin\data\db
	class Meta:
		model = ArtsUser
		fields = (
			'id',
			'username',
			'password',
			'email',
			'createtime',
			'flag'
		)



class TagSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tag
		fields = (
			"id",
			't_name',
			't_info',
			't_createtime',
			't_flag',
		)

class ArtSerializer(serializers.HyperlinkedModelSerializer):

	operator = serializers.ReadOnlyField(source="operator.username")

	class  Meta:
		model = Art
		fields = (
			"id",
			"a_title",
			"a_info",
			"a_content",
			"a_img",
			"a_createtime",
			"a_tag",
			"a_price",
			"a_flag",
            "operator",
		)




class ChapterSerializer(serializers.HyperlinkedModelSerializer):

	class  Meta:
		model = Chapter
		fields = (
			"id",
			"art",
			"title",
			"content",
			"create_time",
		)


class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):

	class  Meta:
		model = ProductOrder
		fields = (
			"id",
			"order_id",
			"pay_type",
			"address",
			"phone",
			"order_time",
		)



class LineItemSerializer(serializers.HyperlinkedModelSerializer):

	class  Meta:
		model = LineItem
		fields = (
			"id",
			"product",
			"user",
			"unit_price",
			"quantity",
			"createtime",
			'product_order',
			'flag',
		)



class CommentSerializer(serializers.HyperlinkedModelSerializer):

	class  Meta:
		model = Comment
		fields = (
			"id",
			"name",
			"title",
			"text",
			"created_time",
			"art",
			'flag',
		)
