from django.urls import path

from users.views import (
	CreateUserAPIView,
	UserLoginAPIView,
)

from farmers.views import (
	SingleFarmerAPIView,
	CreateFarmersView,
	FarmerByUsedView,
)


urlpatterns = [
	path('auth/signup', CreateUserAPIView.as_view(), name="signup"),
	path('auth/login', UserLoginAPIView.as_view(), name="login"),
	path('farmers/<int:pk>', SingleFarmerAPIView.as_view(),
		name="farmer_detail"),
	path('farmers', CreateFarmersView.as_view(), name="farmers_list"),
	path('farmers/users/<int:pk>', FarmerByUsedView.as_view(), 
		name="user_farmers"),
]
