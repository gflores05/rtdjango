from django.db import models
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel


class Player(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    nickname = models.CharField(
        max_length=50, unique=True, verbose_name=_("Nickname")
    )
    level = models.IntegerField(default=0, verbose_name=_("Level"))
    points = models.IntegerField(default=0, verbose_name=_("Points"))

    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")

    def __str__(self):
        return f"{self.id} - {self.name}({self.nickname})"
