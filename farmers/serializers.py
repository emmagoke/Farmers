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


class RegisterFarmerSerializer(serializers.Serializer):
	first_name = serializers.CharField(max_length=50)
	last_name = serializers.CharField(max_length=50)
	phone_number = serializers.CharField(max_length=14)
	birth_date = serializers.DateTimeField()
	address = serializers.CharField(max_length=150)
	crops = serializers.CharField(max_length=150)
	season_best_for_crops = serializers.CharField(max_length=15)
	# user_id = serializers.PrimaryKeyRelatedField(query=User.objects.all())

	def create(self, validated_data):
		farmer_list = Farmer(**validated_data)
		farmer_list.save()
		return farmer_list
