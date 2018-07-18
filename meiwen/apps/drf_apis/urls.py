# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/7/7 下午7:57' 
from django.conf.urls import url, include

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from drf_apis import view_set

schema_view = get_schema_view(title="小说平台 APIs 摘要信息")


#for viewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('art_user', view_set.ArtsUserViewSet)
router.register('tag', view_set.TagViewSet)
router.register('art', view_set.ArtViewSet)
router.register('chapter', view_set.ChapterViewSet)
router.register('product_order', view_set.ProductOrderViewSet)
router.register('line_item', view_set.LineItemViewSet)
router.register('comment', view_set.CommentViewSet)

urlpatterns = [
   url(r'^', include(router.urls)),
   url(r'docs/', include_docs_urls(title="小说电商平台")),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]