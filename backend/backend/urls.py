from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'comments', views.CommentsView, 'comments')
router.register(r'userfollowing', views.UserFollowingViewSet, 'userfollowing')
router.register(r'userfollower', views.UserFollowerViewSet, 'userfollower')
router.register(r'users', views.UserView, 'users')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/auth/myuser/', views.UserAPI.as_view())
]

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name="index.html"))]
