from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

#from service.something_update import send_order_email, send_order_email_1
from apscheduler.triggers.combining import OrTrigger
#from apscheduler.triggers.interval import CalendarIntervalTrigger
from apscheduler.triggers.combining import AndTrigger
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from service.models import Mailing, Logs
from datetime import datetime


# Функция используется для рассылки писем
def send_order_email(pk_mailing, ):
    list_email = []
    for item in Mailing.objects.all():
        if item.pk == int(pk_mailing):
            for cl in item.client.all():
                list_email.append(cl.email)
            if item.status != 'завершена':
                for email in list_email:
                    try:
                        Mailing.objects.filter(id=item.id).update(status='запущена')
                        send_mail(
                            f'{item.message.title}',
                            f'{item.message.text}',
                            settings.EMAIL_HOST_USER,
                            [email],
                            # ['dgdgfdgsg'],
                            # ['albert.minnibaeff@yandex.ru'],
                            fail_silently=False,
                        )
                    except:
                        Mailing.objects.filter(id=item.id).update(status='создана')
                        print(f'Не удалось отравить сообщение "{item.message.title}" на адрес "{email}"')
                        Logs.objects.create(data_time=datetime.now(), status='Неуспешно', message=item.message)
                    else:
                        Mailing.objects.filter(id=item.id).update(status='создана')
                        Logs.objects.create(data_time=datetime.now(), status='Успешно', message=item.message)


# Функция используется для задания периодичности рассылки писем при создании рассылки
def start_1(item):
    scheduler = BackgroundScheduler()
    if item.frequency == 'раз в день':
        #trigger = OrTrigger([CronTrigger(second=item.time.second, minute='*')])
        trigger = OrTrigger([CronTrigger(hour=item.time.hour, minute=item.time.minute, second=item.time.second)])
                                         #day='*')])
    elif item.frequency == 'раз в неделю':
        trigger = OrTrigger([CronTrigger(hour=item.time.hour, minute=item.time.minute, second=item.time.second,
                                         week='*')])
    elif item.frequency == 'раз в месяц':
        trigger = OrTrigger([CronTrigger(hour=item.time.hour, minute=item.time.minute, second=item.time.second,
                                         month='*')])
    scheduler.add_job(send_order_email, trigger, (str(item.pk),))
    #scheduler.add_job(send_order_email_1, trigger, args=item)
    #scheduler.add_job(send_order_email, next_run_time=datetime(2023, 9, 23, 0, 30, 0), misfire_grace_time=120)# 'interval', seconds=10)
    scheduler.start()


# Функция используется для рассылки писем при запуске программы
def start():
    for item in Mailing.objects.all():
        start_1(item)


# Функция используется для рассылки писем при ручном запуске
def send_order_email_1():
    for item in Mailing.objects.all():
        list_email = []
        for cl in item.client.all():
            list_email.append(cl.email)
        if item.status != 'завершена':
            for email in list_email:
                try:
                    Mailing.objects.filter(id=item.id).update(status='запущена')
                    send_mail(
                        f'{item.message.title}',
                        f'{item.message.text}',
                        settings.EMAIL_HOST_USER,
                        [email],
                        #['dgdgfdgsg'],
                        #['albert.minnibaeff@yandex.ru'],
                        fail_silently=False,
                    )
                except:
                    Mailing.objects.filter(id=item.id).update(status='создана')
                    print(f'Не удалось отравить сообщение "{item.message.title}" на адрес "{email}"')
                    Logs.objects.create(data_time=datetime.now(), status='Неуспешно', message=item.message)
                else:
                    Mailing.objects.filter(id=item.id).update(status='создана')
                    Logs.objects.create(data_time=datetime.now(), status='Успешно', message=item.message)


# def start():
    # scheduler = BackgroundScheduler()
    # trigger = OrTrigger([CronTrigger(hour=20, minute=29), CronTrigger(hour=23, minute=10)])
    # scheduler.add_job(send_order_email, trigger)
    # #scheduler.add_job(send_order_email, next_run_time=datetime(2023, 9, 23, 0, 30, 0), misfire_grace_time=120)# 'interval', seconds=10)
    # scheduler.start()
