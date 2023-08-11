# from celery import shared_task
from django.core.mail import send_mail
from assessment.celery import app
from celery.schedules import crontab
from sms import send_sms

from .models import Farmer


@app.task
def weather_report_for_farmer():
    # Mock a weather report based on the season
    weather_report = {
        'rainy': 'It is going to rain this morning. Good time to plant your crops.',
        'dry': 'It is dry and sunny today. Good time to harvest your crops.'
    }
    
    farmers = Farmer.objects.all()
    # Loop through each farmer
    for farmer in farmers:
        season = farmer.season_best_for_crops.split('/')[0]
        # print(season)
        report = weather_report[season]
        send_mail(
            subject='Weather Report',
            message=report,
            from_email='weather@report.com',
            recipient_list=[farmer.phone_number],
            # fail_silently=False,
        )
        # send_sms(report, farmer.phone_number,
        #     backend='django_sms.backends.console.SmsBackend')
        # # Print the weather report on the console
        print(f'Sent weather report to {farmer.name}: {report}')


# # Schedule the task to run every day at 7am using crontab
# app.conf.beat_schedule = {
#     'send-weather-report': {
#         'task': 'tasks.weather_report_for_farmer',
#         'schedule': crontab(hour=17, minute=56),
#     },
# }

# app.conf.timezone = 'Africa/Lagos'