from django.dispatch import receiver
from django.db.models.signals import post_save
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


# Create your models here.

# Create your models here.


class Score(models.Model):
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    score_type = models.CharField(max_length=32, blank=False, null=False)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    communities = models.ManyToManyField(
        'Community', blank=True, related_name="communities")
    score = models.OneToOneField(Score, on_delete=models.CASCADE)
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         team = Team.objects.create(name=instance.username + "'s team")
#         instance.profile.teams.add(team)
#         instance.save()


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Community(MPTTModel):
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.CharField(max_length=2048, blank=False, null=False)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile")
    score = models.ForeignKey(
        Score, on_delete=models.CASCADE, related_name="community_score")
    parent_communities = TreeForeignKey('self', on_delete=models.CASCADE,
                                        null=True, blank=True, related_name='child_communities')


class Post(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.CharField(max_length=2048, blank=False, null=False)
    link = models.CharField(max_length=256, blank=True, null=True)
    post_type = models.CharField(max_length=32, blank=False, null=False)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE)  # models.SET_NULL
    communities = models.ManyToManyField(
        'Community', related_name="post_communities")
    created = models.DateTimeField(auto_now=True)
    # image field here
    score = models.ForeignKey(
        Score, on_delete=models.CASCADE, related_name="score")


class Comment(models.Model):
    content = models.CharField(max_length=256, blank=False, null=False)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE)  # models.SET_NULL
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    score = models.ForeignKey(
        Score, on_delete=models.CASCADE, related_name="comment_score")
    created = models.DateTimeField(auto_now=True)
