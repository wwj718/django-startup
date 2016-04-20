#!/usr/bin/env python
# encoding: utf-8

import views
#from rest_framework.routers import DefaultRouter
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
#router = DefaultRouter()
router = DefaultRouter()
router.register(r'snappets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
