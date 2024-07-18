from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as JwtTokenObtainPairSerializer,
)
from django.db.models import Q

from .models import User


class CustomTokenObtainPairSerializer(JwtTokenObtainPairSerializer):
	
	@classmethod
	def get_token(cls, user):
		
		token = super().get_token(user)
		
		# Add custom claims
		token["user_id"] = user.id
		token["email"] = user.email
		token["phone_number"] = user.phone_number
		token["first_name"] = user.first_name
		token["last_name"] = user.last_name
		token["is_admin"] = user.is_admin
		token["is_superuser"] = user.is_superuser
		
		return token
	
	def authenticate_user(self, username, password):
		""" This method check if the user exists and the password is correct """
		try:
			user = User.objects.get(Q(email=username) | Q(phone_number=username))
		except User.DoesNotExist:
			user = None
		
		if user is not None and user.check_password(password):
			return user		

		return None
	
	def validate(self, attrs):
		""" The username can be an email or phone_number."""
		username = attrs["username"]
		password = attrs["password"]

		user = self.authenticate_user(username, password)

		if user is None:
			raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )
		
		data = dict()
		refresh = self.get_token(user)
		data["refresh"] = str(refresh)
		data["access"] = str(refresh.access_token)
		return data


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
