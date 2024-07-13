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


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if first_name is None:
            raise TypeError("User must have first_name")
        if last_name is None:
            raise TypeError("User must have last_name")
        if email is None:
            raise TypeError("User must have email.")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, first_name, last_name, email, password=None, **extra_fields
    ):
        user = self.create_user(first_name, last_name, email, password, **extra_fields)

        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.is_verified = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
	email = models.CharField(max_length=254)
	phone_number = models.CharField(max_length=14, unique=True)