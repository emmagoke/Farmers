from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

from .models import Farmer
from users.helpers import filter_phone_number

User = get_user_model()

class FarmerSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	first_name = serializers.CharField(max_length=50)
	last_name = serializers.CharField(max_length=50)
	phone_number = serializers.CharField(max_length=14)
	birth_date = serializers.DateTimeField()
	address = serializers.CharField(max_length=150)
	crops = serializers.CharField(max_length=150)
	season_best_for_crops = serializers.CharField(max_length=15)
	user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


class RegisterFarmerSerializer(serializers.Serializer):
	first_name = serializers.CharField(max_length=50)
	last_name = serializers.CharField(max_length=50)
	phone_number = serializers.CharField(max_length=14)
	birth_date = serializers.DateTimeField()
	address = serializers.CharField(max_length=150)
	crops = serializers.CharField(max_length=150)
	season_best_for_crops = serializers.CharField(max_length=15)
	# user_id = serializers.PrimaryKeyRelatedField(query=User.objects.all())

	def validate_phone_number(self, value):
		return filter_phone_number(value)

	def create(self, validated_data):
		user = self.context.get("user")
		validated_data["user"] = user
		farmer_list = Farmer(**validated_data)
		farmer_list.save()
		return farmer_list
