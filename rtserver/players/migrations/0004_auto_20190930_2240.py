# Generated by Django 2.2.5 on 2019-09-30 22:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20190930_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 30, 22, 40, 42, 870831, tzinfo=utc), verbose_name='Creation date'),
        ),
    ]
