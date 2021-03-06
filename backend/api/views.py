from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CommentSerializer, FollowingSerializer, FollowersSerializer, UserSerializer, ScoreSerializer, PostSerializer, PortfolioSerializer, InvestmentSerializer, InstrumentSerializer
from .models import Comment, UserFollowing, Score, Post, Portfolio, Investment, Instrument
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.contrib.auth import get_user_model
# Create your views here.
UserModel = get_user_model()


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserFollowingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = FollowingSerializer
    queryset = UserFollowing.objects.all()


class UserFollowerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # permission_classes = (IsAuthenticated,)
    serializer_class = FollowersSerializer
    queryset = UserFollowing.objects.all()


class UserAPI(generics.RetrieveAPIView):
    # this is a test for how to gain access with a token
    # first get token
    # then send bodyless get with header:
    # content type :app/json
    # Authorization: JWT {TOKEN HERE}
    #ACCEPT: Application/json
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class ScoresView(viewsets.ModelViewSet):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()


class CommentsView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class PostsView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PortfoliosView(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()


class InvestmentsView(viewsets.ModelViewSet):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()


class InstrumentsView(viewsets.ModelViewSet):
    serializer_class = InstrumentSerializer
    queryset = Instrument.objects.all()
