from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer #, UserSerializer
#from oauth2_provider.ext.rest_framework import OAuth2Authentication
from rest_framework.authentication import SessionAuthentication,TokenAuthentication

class PostViewSet(viewsets.ModelViewSet):
    """"""
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    queryset =Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                                      IsOwnerOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

'''
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    """
    authentication_classes = (TokenAuthentication, SessionAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
'''
