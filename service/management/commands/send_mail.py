from django.core.management import BaseCommand

from service.services import send_order_email


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_order_email()
