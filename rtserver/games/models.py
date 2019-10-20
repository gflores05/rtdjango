from django.db import models
from players.models import Player
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=15, default='', unique=True)
    description = models.CharField(max_length=250)
    created = models.DateTimeField('Creation date', default=timezone.now())
    def __str__(self):
        return self.name

class GameResult(models.Model):
    #If null, game was tied
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, default=None, blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    """
    0 - Resolved
    1 - Tie
    2 - Unfinished
    """
    result = models.IntegerField(default=2)
    start = models.DateTimeField('Game start date', default=timezone.now())
    end = models.DateTimeField('Game end date', null=True, default=None, blank=True)
    state = models.CharField()

    def str_status(self):
        status = ['resolved', 'tie', 'unfinished']
        return status[self.result]

    def __str__(self):
        result = "{0} - Game {1}, winner: {2}, status: {3}"
        return result.format(self.id, self.game.name, self.winner.name if self.winner != None else "nobody", self.str_status())

class GameResultDetail(models.Model):
    result = models.ForeignKey(GameResult, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        detail = "{0} Game {1}, player: {2}, points: {3}"
        return detail.format(self.result.id, self.result.game.name, self.player.name, self.points)
