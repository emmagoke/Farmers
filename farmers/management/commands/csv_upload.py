"""
This script handles the upload csv generated file to any third party media
hosting platform and
return the link to the csv file on the console.
"""
from django.core.management.base import BaseCommand, CommandError
from farmers.models import Farmer
import requests
from datetime import datetime
from os import getenv

import csv

class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument('url', type="str",
			help="This indicate the url you want to upload to")


	def handle(self, *args, **kwargs):
		url = kwargs.get('url', None)
		if url is None:
			raise CommandError('You must supply the url fields')
		farmers = Farmer.objects.all()
		fields = [ field.name for field in Farmer._meta.get_fields()]
		file_name = "farmer_upload_{}_{}_{}.csv".format(
			datetime.now().year, datetime.now().month, datetime.now().day)
		with open(file_name, 'w') as file:
			writer = csv.writer(file)
			writer.writerow(fields[:-1])

			for farmer in farmers:
				writer.writerow([farmer.id, farmer.first_name, farmer.last_name,
					farmer.phone_number, farmer.age, farmer.address, farmer.crops,
					farmer.season_best_for_crops])
		file_up = open(file_name, 'rb')

		url = url
		files = {"file": file_up}
		username = getenv('USERNAME', '')
		password = getenv('PASSWORD', '')
		payload={username: username, password: password}
		try:
			response = requests.post(url, files=files, data=payload)
			self.stdout(response.json()['url'])
		except Exception as error:
			self.stdout.write(error)
		finally:
			os.remove(file_name)
