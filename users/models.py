from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# Create your models here.
class CustomUser(AbstractUser):
	email = models.CharField(max_length=254)
	phone_number = models.CharField(max_length=14, unique=True)