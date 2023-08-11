""" This script contains a method that runs cron job"""
from sms import send_sms
from .models import Farmer

# Mock a weather report based on the season
weather_report = {
    'rainy': 'It is going to rain this morning. Good time to plant your crops.',
    'dry': 'It is dry and sunny today. Good time to harvest your crops.'
}


def send_message():
	
    farmers = Farmer.objects.all()
    print("cron")
    for farmer in farmers:
        season = farmer.season_best_for_crops.split('/')[0]
        report = weather_report[season]
        # send_mail(
        #     subject='Weather Report',
        #     message=report,
        #     from_email='weather@report.com',
        #     recipient_list=[farmer.phone_number],
        #     # fail_silently=False,
        # )
        send_sms(report,"08062924255",  farmer.phone_number)
        # # Print the weather report on the console
        print(f'Sent weather report to {farmer.name}: {report}')