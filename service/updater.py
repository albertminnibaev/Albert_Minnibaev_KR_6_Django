from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from service.something_update import send_order_email, send_order_email_1
from apscheduler.triggers.combining import OrTrigger
#from apscheduler.triggers.interval import CalendarIntervalTrigger
from apscheduler.triggers.combining import AndTrigger
from datetime import datetime


def start():
    scheduler = BackgroundScheduler()
    trigger = OrTrigger([CronTrigger(hour=20, minute=29), CronTrigger(hour=23, minute=10)])
    scheduler.add_job(send_order_email, trigger)
    #scheduler.add_job(send_order_email, next_run_time=datetime(2023, 9, 23, 0, 30, 0), misfire_grace_time=120)# 'interval', seconds=10)
    scheduler.start()


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
    scheduler.add_job(send_order_email_1, trigger, (str(item.pk),))
    #scheduler.add_job(send_order_email_1, trigger, args=item)
    #scheduler.add_job(send_order_email, next_run_time=datetime(2023, 9, 23, 0, 30, 0), misfire_grace_time=120)# 'interval', seconds=10)
    scheduler.start()


