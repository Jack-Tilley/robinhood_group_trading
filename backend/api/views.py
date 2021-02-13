from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentSerializer, FollowingSerializer, FollowersSerializer, UserSerializer
from .models import Comment, UserFollowing
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model
# Create your views here.
UserModel = get_user_model()


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserFollowingViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FollowingSerializer
    queryset = UserFollowing.objects.all()


class UserFollowerViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FollowersSerializer
    queryset = UserFollowing.objects.all()


class CommentsView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
