from django.contrib import admin

from service.models import Client, Mailing, Message, Logs
from service.services import start_1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'frequency', 'status')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        start_1(obj) # для запуска рассылки при создании через админку


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('data_time', 'status', 'answer', 'message')
