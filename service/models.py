from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    title = models.CharField(max_length=250, verbose_name='тема письма')
    text = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='почта', unique=True)
    comment = models.CharField(**NULLABLE, verbose_name='комментарий')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='создатель')
    #mailing = models.ManyToManyField(Mailing)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):
    #title = models.CharField(default='mailing', max_length=250, verbose_name='тема')
    status_param = (('создана','создана'), ('запущена','запущена'), ('завершена','завершена'),)
    frequency_param = (('раз в день', 'раз в день'), ('раз в неделю', 'раз в неделю'), ('раз в месяц', 'раз в месяц'),)
    time = models.TimeField(verbose_name='время рассылки')
    frequency = models.CharField(default=1, max_length=30, verbose_name='периодичность', choices=frequency_param)
    status = models.CharField(default=1, max_length=30, verbose_name='статус рассылки(завершена, создана, '
                                                                             'запущена)',
                              choices=status_param)
    message = models.ForeignKey(Message, **NULLABLE, on_delete=models.CASCADE, verbose_name='сообщение')
    client = models.ManyToManyField(Client)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='создатель')

    def __str__(self):
        return f'{self.time} ({self.frequency})'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Logs(models.Model):
    data_time = models.DateTimeField(**NULLABLE, verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=15, verbose_name='статус попытки')
    answer = models.CharField(**NULLABLE, max_length=250, verbose_name='ответ почтового сервера')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')

    def __str__(self):
        return f'{self.data_time} ({self.status})'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
