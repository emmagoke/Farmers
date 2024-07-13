from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomUser(AbstractUser):
	email = models.CharField(max_length=254)
	phone_number = models.CharField(max_length=14, unique=True)