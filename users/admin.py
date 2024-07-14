from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
	add_form = UserCreationForm
	form = UserChangeForm
	model = User
	list_display = [
		'email',
		'phone_number',
		"first_name",
        "last_name",
        "created_at",
        "updated_at",
        "is_admin",
        "is_staff",
        "is_active",
	]
	fieldsets = (
		(None, {"fields": ("phone_number", "email", "password")}),
		(
			"Personal info",
			{
				"fields": 
					("first_name", "last_name")
			}
		),
		(
			"Permissions", 
			{
				"fields": (
					"is_admin",
					"is_verified",
					"is_active",
					"is_staff",
				)
			})
	)
	# This is the field displayed when a new user is to be created
	# on the django admin
	add_fieldsets = (
		(
			None, 
			{
				"fields": (
					"phone_number", "email",
					"first_name", "last_name",
					"password1", "password2",
				)
			}
		),
		(
			"Permissions",
			{
				"fields": (
					"is_admin",
					"is_verified",
					"is_active",
					"is_staff",
				)
			}
		),
	)
	ordering = ("email",)

admin.site.register(User, CustomUserAdmin)
