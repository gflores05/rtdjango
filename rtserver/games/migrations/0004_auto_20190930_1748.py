# Generated by Django 2.2.5 on 2019-09-30 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0003_auto_20190930_1747"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 9, 30, 17, 48, 36, 874303),
                verbose_name="Creation date",
            ),
        ),
        migrations.AlterField(
            model_name="gameresult",
            name="start",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 9, 30, 17, 48, 36, 875583),
                verbose_name="Game start date",
            ),
        ),
    ]
