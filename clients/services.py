from datetime import datetime

# import schedule
# import time
from django.core.mail import send_mail

from clients.models import Mailings, Log
from config import settings


def mailing_create_day():
    """Отправка сообщений"""

    mailings = Mailings.objects \
        .filter(status="создано") \
        .filter(date__lte=datetime.today()) \
        .filter(time__lte=datetime.now()) \
        .filter(period='день')

    for mailing in mailings:
        mailing.status = 'в процессе'
        mailing.save()
        clients = mailing.clients.all()
        mails = mailing.mail_set.all()

        for client in clients:
            response = 0
            print(client.email)

            for mail in mails:
                try:
                    response = send_mail(
                        subject=mail.subject,
                        message=mail.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                    )
                except Exception as e:
                    print(e)
            status = "завершено" if response else "неудачно"
            log = Log(answer_server=response, status=status, mailing=mailing)
            log.save()

        mailing.status = 'создано'
        mailing.save()


def mailing_create_week():
    """Отправка сообщений"""

    mailings = Mailings.objects \
        .filter(status="создано") \
        .filter(date__lte=datetime.today()) \
        .filter(time__lte=datetime.now()) \
        .filter(period='неделя')

    for mailing in mailings:
        mailing.status = 'в процессе'
        mailing.save()
        clients = mailing.clients.all()
        mails = mailing.mail_set.all()

        for client in clients:
            response = 0

            for mail in mails:
                try:
                    response = send_mail(
                        subject=mail.subject,
                        message=mail.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                    )
                except Exception as e:
                    print(e)
            status = "завершено" if response else "неудачно"
            log = Log(answer_server=response, status=status, mailing=mailing)
            log.save()

        mailing.status = 'создано'
        mailing.save()


def mailing_create_month():
    """Отправка сообщений"""

    mailings = Mailings.objects \
        .filter(status="создано") \
        .filter(date__lte=datetime.today()) \
        .filter(time__lte=datetime.now()) \
        .filter(period='месяц')

    for mailing in mailings:
        mailing.status = 'в процессе'
        mailing.save()
        clients = mailing.clients.all()
        mails = mailing.mail_set.all()

        for client in clients:
            response = 0

            for mail in mails:
                try:
                    response = send_mail(
                        subject=mail.subject,
                        message=mail.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                    )
                except Exception as e:
                    print(e)
            status = "завершено" if response else "неудачно"
            log = Log(answer_server=response, status=status, mailing=mailing)
            log.save()

        mailing.status = 'создано'
        mailing.save()
