# Generated by Django 4.2.5 on 2023-09-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_mailing_frequency_alter_mailing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='mailing',
            field=models.ManyToManyField(to='service.mailing'),
        ),
    ]
