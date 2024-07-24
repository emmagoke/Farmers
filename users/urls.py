from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .viewsets import AuthenticationViewset


router  = DefaultRouter()
router.register(r"auth", AuthenticationViewset, basename="auth")

urlpatterns = [
    path("", include(router.urls)),
]
