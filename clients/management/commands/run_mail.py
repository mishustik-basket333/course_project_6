import time

from django.core.management import BaseCommand
import schedule

from clients.services import mailing_create_day, mailing_create_week, mailing_create_month


class Command(BaseCommand):

    def handle(self, *args, **options):
        schedule.every().day.at("10:30").do(mailing_create_day)
        schedule.every(7).days.do(mailing_create_week)
        schedule.every(30).days.do(mailing_create_month)
        # schedule.every(3).seconds.do(mailing_create_day)

        while True:
            schedule.run_pending()
            time.sleep(1)
