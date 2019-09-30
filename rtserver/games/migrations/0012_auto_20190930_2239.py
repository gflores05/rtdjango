# Generated by Django 2.2.5 on 2019-09-30 22:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_auto_20190930_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 22, 39, 56, 957866, tzinfo=utc), verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='gameresult',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 22, 39, 56, 959221, tzinfo=utc), verbose_name='Game start date'),
        ),
    ]