#from django.contrib import admin
import xadmin
# Register your models here.
from arts_app.models import Student, Tag, Art, ArtsUser, Chapter
from message.models import UserMessage
from xadmin import views

class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    #整体配置
    site_title = '美文后台管理系统'
    site_footer = '千锋教育python项目'
    menu_style = 'accordion'    #菜单折叠
    global_search_models = [Student,ArtsUser, Tag, Art, Chapter,UserMessage]
    global_models_icon = {
        Art: "glyphicon glyphicon-book",
        Tag: "fa fa-cloud",
        Chapter:"glyphicon glyphicon-book",
        Student: "glyphicon glyphicon-user",
        ArtsUser: "glyphicon glyphicon-user",
        UserMessage:  "glyphicon glyphicon-list-alt",
    }  # 设置models的全局图标


class StudentAdmin(object):
    list_display = ['name', 'sex', 'address', 'addtime', 'flag']
    search_fields = ['name', 'sex', 'address', 'addtime']
    list_filter = ['name', 'sex', 'address', 'addtime']

class TagAdmin(object):
    list_display = ['t_name', 't_info', 't_createtime', 't_flag']
    search_fields = ['t_name', 't_info', 't_createtime']
    list_filter = ['t_name', 't_info', 't_flag']
    list_editable = ['t_name']


class ArtAdmin(object):
    list_display = ['a_title', 'a_info', 'a_content', 'a_img', 'a_price' ,'a_createtime', 'a_tag']
    search_fields = ['a_title', 'a_info', 'a_content', 'a_img', 'a_createtime']
    list_filter = ['a_title', 'a_info', 'a_createtime', 'a_flag']
    show_detail_fields = ['a_title']
    list_per_page = 5
    list_editable = ['a_title', 'a_info', 'a_price' ,'a_content']
    style_fields = {'a_content': 'ueditor'}


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
class ArtsUserAdmin(object):
    list_display = ('username', 'password', 'email')


class ChapterAdmin(object):
    list_display = ['art', 'title', 'content', 'create_time']
    show_detail_fields = ['art']
    search_fields = ['art', 'title', 'content', 'create_time']
    list_per_page = 5
    list_editable = ['title']



xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)


xadmin.site.register(Student, StudentAdmin)

xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Art, ArtAdmin)
xadmin.site.register(Chapter, ChapterAdmin)

xadmin.site.register(ArtsUser, ArtsUserAdmin)


