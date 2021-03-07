from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()
        return user

        # return self._create_user(email, name, password, **extra_fields)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # THIS MUST BE CHANGED  FOR PROD to FALSE
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


UserModel = get_user_model()


class UserFollowing(models.Model):
    user_id = models.ForeignKey(
        UserModel, related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey(
        UserModel, related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user_id', 'following_user_id'],  name="unique_followers")
        ]
        ordering = ["-created"]

    # def __str__(self):
    #     f"{self.user_id} follows {self.following_user_id}"


class Score(models.Model):
    likes = models.IntegerField(default=0)
    hearts = models.IntegerField(default=0)
    score_type = models.CharField(max_length=32, blank=False, null=False)


class Post(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.CharField(max_length=2048, blank=False, null=False)
    link = models.CharField(max_length=256, blank=True, null=True)
    post_type = models.CharField(max_length=32, blank=False, null=False)
    author = models.ForeignKey(
        UserModel, on_delete=models.CASCADE)  # models.SET_NULL
    # communities = models.ManyToManyField(
    #     'Community', related_name="post_communities")
    created = models.DateTimeField(auto_now=True)
    # image field here
    # score should be updated to OneToOne
    score = models.ForeignKey(
        Score, on_delete=models.CASCADE, related_name="post", blank=True, null=True)


class Comment(models.Model):
    content = models.CharField(max_length=256, blank=False, null=False)
    author = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, related_name="commentor")  # models.SET_NULL
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    # score should be updated to OneToOne
    score = models.ForeignKey(
        Score, on_delete=models.CASCADE, related_name="comments", blank=True, null=True)
    created = models.DateTimeField(auto_now=True)


class Instrument(models.Model):
    instrument_id = models.CharField(
        primary_key=True, max_length=36, blank=False, null=False)
    name = models.CharField(max_length=256, blank=False, null=False)
    symbol = models.CharField(max_length=8, blank=False, null=False)
    tradeable = models.BooleanField()
    list_date = models.DateTimeField(blank=True, null=True)
    market = models.CharField(max_length=256, blank=True, null=True)


class Portfolio(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    user = models.OneToOneField(
        UserModel, on_delete=models.CASCADE)


class Investment(models.Model):
    average_price = models.DecimalField(max_digits=14, decimal_places=4)
    state = models.CharField(max_length=32, blank=True, null=True)
    side = models.CharField(max_length=32, blank=True, null=True)
    quantity = models.DecimalField(max_digits=14, decimal_places=4)
    transaction_total = models.DecimalField(max_digits=14, decimal_places=4)
    created_at = models.DateTimeField(blank=True, null=True)
    finalized_at = models.DateTimeField(blank=True, null=True)
    instrument = models.ForeignKey(
        Instrument, on_delete=models.CASCADE, related_name='investments')
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='investments')
    # check = models.CharField(max_length=32, blank=True, null=True)


class Check(models.Model):
    check = models.CharField(max_length=32, blank=True, null=True)

# class Community(MPTTModel):
#     title = models.CharField(max_length=128, blank=False, null=False)
#     description = models.CharField(max_length=2048, blank=False, null=False)
#     author = models.ForeignKey(
#         Profile, on_delete=models.CASCADE, related_name="profile")
#     score = models.ForeignKey(
#         Score, on_delete=models.CASCADE, related_name="community_score")
#     parent_communities = TreeForeignKey('self', on_delete=models.CASCADE,
#                                         null=True, blank=True, related_name='child_communities')
