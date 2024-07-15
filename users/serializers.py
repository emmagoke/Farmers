from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as JwtTokenObtainPairSerializer,
)

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True,
		required=True, validators=[validate_password])

	class Meta:
		model = CustomUser
		fields = ['id', 'email', 'phone_number', 'password']

	# def validate(self, attrs):
	# 	""" This check if email and phone_number fields are not both empty """
	# 	if attrs.get('email') is None or attrs.get('phone_number') is None :
	# 		raise serializers.ValidationError(
	# 			{"login": "The email and phone_number fields can not null at the same time."}) 

	def create(self, validated_data):
		email, phone_number = None, None
		if validated_data['email']:
			email = validated_data['email']
		if validated_data['phone_number']:
			phone_number = validated_data['phone_number']
		user = CustomUser(
				email=email,
				phone_number=phone_number
			)
		user.set_password(validated_data['password'])
		user.save()

		return user


class LoginSerializer(serializers.Serializer):
	email = serializers.CharField(max_length=254, required=True)
	password = serializers.CharField(max_length=128,
		required=True, write_only=True)

	def validate(self, attrs):
		email = attrs.get('email')
		password = attrs.get('password')
		try:
			user_obj = CustomUser.objects.get(email=email)
		except CustomUser.DoesNotExist:
			user_obj = CustomUser.objects.get(phone_number=email)
		except CustomUser.DoesNotExist:
			message = 'Unable to log in with provided credentials.'
			raise serializers.ValidationError({"authorization": message})
		
		user = authenticate(request=self.context.get('request'),
						username=user_obj.username, password=password)
				
				
		attrs['user'] = user

		return attrs
