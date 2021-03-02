from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Comment, UserFollowing, Post, Score, Investment, Portfolio, Instrument
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


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'likes', 'hearts', 'score_type')


class CommentSerializer(serializers.ModelSerializer):
    # score = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'post', 'score', 'created')

    # def get_score(self, obj):
    #     return ScoreSerializer(obj.score.all(), many=True).data


class PostSerializer(serializers.ModelSerializer):
    # comments = serializers.SerializerMethodField()
    # score = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "description",
            "link",
            "author",
            "score",
            # "post_type",
            "created",
            "comments",
        )

    # def get_comments(self, obj):
    #     return CommentSerializer(obj.comments.all(), many=True).data

    # def get_score(self, obj):
    #     return ScoreSerializer(obj.score.all(), many=True).data


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = (
            "id",
            "name",
            "ticker",
            "full_name",
            "avg_buy_price",
            "avg_sell_price",
            "date_of_purchase",
            "date_of_sale",
            "portfolio_id",
        )


class PortfolioSerializer(serializers.ModelSerializer):
    investments = InvestmentSerializer(source='investment_set', many=True)

    class Meta:
        model = Portfolio
        fields = (
            "id",
            "name",
            "user_id",
            'investments'
        )


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = (
            "id",
            "instrument_id",
            "name",
            "market",
            'tradeable',
            "list_date",
            "symbol",
        )
