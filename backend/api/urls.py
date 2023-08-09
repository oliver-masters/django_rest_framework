from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views


urlpatterns = [
    path('auth/', obtain_auth_token),
    path("", views.api_home, name="api_home"),

]