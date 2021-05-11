from django.db import models
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel, StatusModel, TimeFramedModel
from model_utils import Choices

from players.models import Player


class Game(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    code = models.CharField(max_length=4, unique=True, verbose_name=_("Code"))
    description = models.CharField(
        max_length=250, null=True, verbose_name=_("Description")
    )

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    def __str__(self):
        return f"{self.code} - {self.name}"


class GameResult(TimeStampedModel, StatusModel, TimeFramedModel):
    CHALLENGE = "challenge"
    STARTED = "started"
    PLAYING = "playing"
    RESOLVED = "resolved"
    INDETERMINATED = "indeterminated"
    TIED = "tied"

    STATUS = Choices(
        (CHALLENGE, _("Challenge")),
        (STARTED, _("Started")),
        (PLAYING, _("Playing")),
        (RESOLVED, _("Resolved")),
        (INDETERMINATED, _("Indeterminated")),
        (TIED, _("tied")),
    )
    chanllenger = models.ForeignKey(
        Player,
        on_delete=models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=_("Challenger"),
        related_name="challenger",
    )
    winner = models.ForeignKey(
        Player,
        on_delete=models.DO_NOTHING,
        default=None,
        null=True,
        verbose_name=_("Winner"),
        related_name="winner",
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        verbose_name=_("Game"),
        related_name="game",
    )

    class Meta:
        verbose_name = _("Game Result")
        verbose_name_plural = _("Game Results")

    def __str__(self):
        return f"{self.id} - {self.game.code} ({self.status})"


class GameResultDetail(TimeStampedModel):
    result = models.ForeignKey(
        GameResult,
        on_delete=models.CASCADE,
        related_name="game_result",
        verbose_name=_("Game Result"),
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="player",
        verbose_name=_("Player"),
    )
    points = models.IntegerField(default=0, verbose_name=_("Points"))

    class Meta:
        verbose_name = _("Game Result Detail")
        verbose_name_plural = _("Game Result Details")

    def __str__(self):
        return f"{self.result.game.code} - {self.player.name}: {self.points}"
