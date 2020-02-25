"""virtualmagiciansapi URL Configuration"""
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from virtualmagicians.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user),
    path('login/', login_user),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]