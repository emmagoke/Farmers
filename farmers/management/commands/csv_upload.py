"""
This script handles the upload csv generated file to any third party media
hosting platform and
return the link to the csv file on the console.
"""
from django.core.management.base import BaseCommand, CommandError
from farmers.models import Farmer
from datetime import datetime
import os
from cloudinary.uploader import upload
from farmers.helper import calculate_age

import csv

class Command(BaseCommand):

	# def add_arguments(self, parser):
	# 	parser.add_argument('url', type=str,
	# 		help="This indicate the url you want to upload to")


	def handle(self, *args, **kwargs):
		# url = kwargs.get('url', None)
		# if url is None:
		# 	raise CommandError('You must supply the url fields')
		farmers = Farmer.objects.all()
		# fields = [ field.name for field in Farmer._meta.get_fields()]
		file_name = "farmer_upload_{}_{}_{}.csv".format(
			datetime.now().year, datetime.now().month, datetime.now().day)
		with open(file_name, 'w') as file:
			writer = csv.writer(file)
			writer.writerow(
            	['ID', 'First Name', 'Last Name', 'Phone Number', 'Age', 'Address', 'Crops', 'Best Season']
        	)

			for farmer in farmers:
				age = calculate_age(farmer.birth_date)
				writer.writerow([farmer.id, farmer.first_name, farmer.last_name,
					farmer.phone_number, age, farmer.address, farmer.crops,
					farmer.season_best_for_crops])
		file_up = open(file_name, 'rb')

		try:
			resource_type = "raw" 
			cloud_url = upload(file_up, folder="Farmers", resource_type=resource_type)
			file_url = cloud_url["secure_url"]
			self.stdout.write(file_url)
		except Exception as error:
			self.stdout.write(str(error))
		finally:
			os.remove(file_name)
