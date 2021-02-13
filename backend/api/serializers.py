from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Comment, UserFollowing
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "following_user_id", "created")


class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ("id", "user_id", "created")


class UserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "following",
            "followers",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def get_following(self, obj):
        return len(FollowingSerializer(obj.following.all(), many=True).data)

    def get_followers(self, obj):
        return len(FollowersSerializer(obj.followers.all(), many=True).data)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created')
