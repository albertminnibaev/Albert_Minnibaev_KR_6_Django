from django.conf import settings
from django.core.mail import send_mail
from service.models import Mailing


def send_order_email(item):
    #for item in Mailing.objects.all():
    send_mail(
        'Привет',
        f'{item.message.title}',
        settings.EMAIL_HOST_USER,
        ['albert.minnibaeff@yandex.ru']
    )

# def send_order_email():
#     for item in Mailing.objects.all():
#         print('1')
#         send_mail(
#             'Привет',
#             f'{item.message.title}',
#             settings.EMAIL_HOST_USER,
#             ['albert.minnibaeff@yandex.ru']
#         )

# def send_order_email():
#     send_mail(
#         'Привет',
#         f'ggggggg',
#         settings.EMAIL_HOST_USER,
#         ['albert.minnibaeff@yandex.ru']
#     )