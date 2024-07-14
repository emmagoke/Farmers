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
		'is_staff'
	]
	fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone_number",)}), )
	add_fieldsets = UserAdmin.add_fieldsets + ((None,
		{"fields": ("phone_number", "email", )}), )

admin.site.register(CustomUser, CustomUserAdmin)
