#!/usr/bin/env python
# encoding: utf-8
#from django.contrib.auth.models import User
from rest_server.users.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_server.snippets.models import Snippet
from rest_server.snippets.permissions import IsOwnerOrReadOnly
from rest_server.snippets.serializers import SnippetSerializer, UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.

    The `highlight` field presents a hyperlink to the highlighted HTML
    representation of the code snippet.

    The **owner** of the code snippet may update or delete instances
    of the code snippet.

    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    #参考:http://www.django-rest-framework.org/api-guide/generic-views/
    #queryset - The queryset that should be used for returning objects from this view,Typically, you must either set this attribute, or override the get_queryset() method.
    queryset = Snippet.objects.all()
    #serializer_class - The serializer class that should be used for validating and deserializing input, and for serializing output
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    #Any methods on the viewset decorated with @detail_route or @list_route will also be routed.
    #^users/{pk}/set_password/$
    #URL pattern: ^snippets/{pk}/highlight/$ Name: 'snippet-highlight',出现在对象页面里

    def run_code(self,code):
        #call docker
        return "</hr><h1>{}</h1>".format(code)

    @detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        #能否执行docker，并将执行结果加上去，直接返回html，数据分析也可以
        code_run_result = self.run_code(snippet.code)
        return Response(snippet.highlighted + code_run_result)

    def perform_create(self, serializer):
        #perform_create(self, serializer) - Called by CreateModelMixin when saving a new object instance.
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of snippet instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
