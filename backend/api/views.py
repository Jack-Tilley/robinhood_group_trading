from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentSerializer
from .models import Comment
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.


class CommentsView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
