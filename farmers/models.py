from django.db import models
from django.conf import settings


# Create your models here.
class Farmer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=14, unique=True)
	age = models.PositiveIntegerField()
	address = models.CharField(max_length=150)
	crops = models.CharField(max_length=150)
	season_best_for_crops = models.CharField(max_length=15)
	user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name
