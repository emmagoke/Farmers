from django.contrib import admin

from .models import Farmer
# Register your models here.

class FarmerAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'birth_date']

admin.site.register(Farmer, FarmerAdmin)