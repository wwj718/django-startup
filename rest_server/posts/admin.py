#coding:utf-8
from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    fields = ("owner","title","content")
    list_display = ("owner","title","content")
    ordering = ('-create_time', )

admin.site.register(Post, PostAdmin)
