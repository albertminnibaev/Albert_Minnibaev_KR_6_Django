from django.apps import AppConfig

#from service import services


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'
    verbose_name = 'Сервис рассылок'

    def ready(self):
        from service import services
        services.start()


# class RoomConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'room'
#
#     def ready(self):
#         from service import updater
#         updater.start()

