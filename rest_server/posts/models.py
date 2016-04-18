#coding:utf-8
from __future__ import unicode_literals
from django.db import models
#from django.contrib.auth.models import User
from rest_server.users.models import User

class Post(models.Model):
    owner = models.ForeignKey(User, related_name='post')
    title = models.CharField(max_length=100, blank=True, default='',verbose_name=u'标题')
    content = models.TextField()
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        ordering = ('create_time',)
# Create your models here.
