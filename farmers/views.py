from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions
from rest_framework_csv.renderers import CSVRenderer
from users.models import User


from .serializers import (
	RegisterFarmerSerializer,
	FarmerSerializer,
)
from .models import Farmer


# Create your views here.
class SingleFarmerAPIView(generics.RetrieveAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	queryset = Farmer.objects.all()
	serializer_class = FarmerSerializer


class ListCreateFarmersView(generics.ListCreateAPIView):
	""" This view Create"""
	permission_classes = (permissions.IsAuthenticated, )
	queryset = Farmer.objects.all()
	serializer_class = RegisterFarmerSerializer
	search_fields = '__all__'

	#  For Bulk insertion implementing ListSerializer
	def get_serializer(self, *args, **kwargs):
		if isinstance(kwargs.get("data", {}), list):
			kwargs["many"] = True

		return super(ListCreateFarmersView, self).get_serializer(*args, **kwargs)


class FarmerByUsedView(generics.ListAPIView):
	""" download list of all farmers a certain user has created as a csv file"""
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = FarmerSerializer
	renderer_classes = [CSVRenderer]

	def get_queryset(self):
		user_id = self.kwargs['pk']
		user = get_object_or_404(User, id=user_id)
		farmers_obj = Farmer.objects.filter(user_id=user)
		return farmers_obj
