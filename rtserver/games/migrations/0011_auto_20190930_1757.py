# Generated by Django 2.2.5 on 2019-09-30 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_auto_20190930_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 17, 57, 17, 661305), verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='gameresult',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 17, 57, 17, 662254), verbose_name='Game start date'),
        ),
    ]
