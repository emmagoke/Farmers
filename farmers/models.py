from django.db import models
from django.conf import settings

from users.models import TimeStamp

# Create your models here.
class Farmer(TimeStamp):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=14, unique=True)
	birth_date = models.DateTimeField(null=True)
	address = models.CharField(max_length=150)
	crops = models.CharField(max_length=150)
	season_best_for_crops = models.CharField(max_length=15)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name
