# Generated by Django 2.2.5 on 2019-09-30 17:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0002_auto_20190930_1743"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 9, 30, 17, 47, 17, 101894),
                verbose_name="Creation date",
            ),
        ),
        migrations.AlterField(
            model_name="gameresult",
            name="result",
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name="gameresult",
            name="start",
            field=models.DateTimeField(
                default=datetime.datetime(2019, 9, 30, 17, 47, 17, 102906),
                verbose_name="Game start date",
            ),
        ),
        migrations.AlterField(
            model_name="gameresult",
            name="winner",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="players.Player",
            ),
        ),
    ]
