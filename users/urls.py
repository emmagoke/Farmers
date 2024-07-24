from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import AuthenticationViewset


router  = DefaultRouter()
router.register(r"auth", AuthenticationViewset, basename="auth")

urlpatterns = [
    path("", include(router.urls)),
]
