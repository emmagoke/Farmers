from django.urls import path

# from users.views import (
# 	CreateUserAPIView,
# 	UserLoginAPIView,
# )

from farmers.views import (
	SingleFarmerAPIView,
	ListCreateFarmersView,
	FarmerByUsedView,
)

from drf_spectacular.views import (
	SpectacularAPIView,
	SpectacularRedocView,
	SpectacularSwaggerView,
)


urlpatterns = [
	# path('auth/signup', CreateUserAPIView.as_view(), name="signup"),
	# path('auth/login', UserLoginAPIView.as_view(), name="login"),
	path('farmers/<int:pk>', SingleFarmerAPIView.as_view(),
		name="farmer_detail"),
	path('farmers', ListCreateFarmersView.as_view(),
		name="farmers_list_create"),
	path('farmers/users/<int:pk>', FarmerByUsedView.as_view(), 
		name="user_farmers"),
	path("schema/", SpectacularAPIView.as_view(), name="schema"),
	path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"),
		name="redoc",),
	path("schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"),
		name="swagger-ui"),
    # path("create", CreateUserAPIView.as_view(), name="create-user"),
]
