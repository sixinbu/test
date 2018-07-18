#from django.contrib import admin

import xadmin
# Register your models here.
from .models import UserMessage


class UserMessageAdmin(object):
    list_display = ['name', 'email', 'address', 'message', 'create_time']
    search_fields = ['name', 'email', 'address']
    list_filter = ['name', 'email', 'address', 'create_time']
    list_per_page = 2
    editable = ['name', 'email']
    style_fields = {'message': 'ueditor'}


xadmin.site.register(UserMessage, UserMessageAdmin)



