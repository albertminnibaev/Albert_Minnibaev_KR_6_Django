# Generated by Django 4.2.5 on 2023-09-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_remove_client_mailing_mailing_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='time',
            field=models.TimeField(verbose_name='время рассылки'),
        ),
    ]