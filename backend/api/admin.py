from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UserFollowing
# from .models import
User = get_user_model()

# Register your models here.
admin.site.register(User)
admin.site.register(UserFollowing)
