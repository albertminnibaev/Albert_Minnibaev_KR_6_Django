from django.contrib import admin

from service.models import Client, Mailing, Message, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'frequency', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('data_time', 'status', 'answer', 'message')
