from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SingleFarmerAPIView,
    ListCreateFarmersView,
    FarmerByUsedView,
)
from .viewsets import FarmersViewset


router  = DefaultRouter()
router.register(r"farmers", FarmersViewset, basename="farmers")

urlpatterns = [
    path("", include(router.urls)),
#     path('farmers/<int:pk>', SingleFarmerAPIView.as_view(),
#          name="farmer_detail"),
#     path('farmers', ListCreateFarmersView.as_view(),
#          name="farmers_list_create"),
#     path('farmers/users/<int:pk>', FarmerByUsedView.as_view(), 
#          name="user_farmers"),
]
