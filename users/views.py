from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


from .models import CustomUser
from .serializers import UserSerializer, LoginSerializer
# Create your views here.

class CreateUserAPIView(generics.CreateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer


class UserLoginAPIView(APIView):

	def post(self, request, *args, **kwargs):
		serializer = LoginSerializer(data=request.data,
			context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		refresh = RefreshToken.for_user(user)
		return Response({
			'refresh': str(refresh),
			'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
