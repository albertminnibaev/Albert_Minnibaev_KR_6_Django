from django.conf import settings
from django.core.mail import send_mail
from service.models import Mailing, Logs
from datetime import datetime


# def update_something():
#     print("this function runs every 10 seconds")

def send_order_email():
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


def send_order_email_1(pk_mailing, ):
    print(pk_mailing)
    list_email = []
    for item in Mailing.objects.all():
        if item.pk == int(pk_mailing):
            for cl in item.client.all():
                list_email.append(cl.email)
            print(list_email)
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

# def send_order_email_1(pk_message, pk_mailing):
#     print(pk_mailing)
#     list_email = []
#     for item in Mailing.objects.all():
#         if item.pk == int(pk_mailing):
#             for cl in item.client.all():
#                 list_email.append(cl.email)
#     for item in Message.objects.all():
#         if item.pk == int(pk_message):
#             send_mail(
#                 f'{item.title}',
#                 f'{item.text}',
#                 settings.EMAIL_HOST_USER,
#                 list_email,
#             )
