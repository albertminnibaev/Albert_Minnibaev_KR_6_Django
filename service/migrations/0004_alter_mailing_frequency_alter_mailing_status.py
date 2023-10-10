# Generated by Django 4.2.5 on 2023-09-22 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_mailing_frequency_alter_mailing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='frequency',
            field=models.IntegerField(choices=[('1', 'раз в день'), ('2', 'раз в неделю'), ('3', 'раз в месяц')], default='раз в день', max_length=1, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('1', 'создана'), ('2', 'запущена'), ('3', 'завершена')], default='создана', max_length=1, verbose_name='статус рассылки(завершена, создана, запущена)'),
        ),
    ]
