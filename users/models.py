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


class User(AbstractBaseUser, PermissionsMixin, TimeStamp):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=254, unique=True)
    last_login = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=14, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
