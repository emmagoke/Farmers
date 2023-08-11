from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Farmer

class FarmerSerializer(serializers.ModelSerializer):
	user_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = Farmer
		fields = [
			'id', 'first_name',
			'last_name', 'phone_number',
			'age', 'address',
			'crops', 'season_best_for_crops', 'user_id'
		]


class RegisterFarmerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Farmer
		fields = [
			'id', 'first_name',
			'last_name', 'phone_number',
			'age', 'address',
			'crops', 'season_best_for_crops', 'user_id'
		]

	def create(self, validated_data):
		farmer_list = Farmer(**validated_data)
		farmer_list.save()
		return farmer_list
