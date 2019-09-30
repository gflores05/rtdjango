from django.db import models
from players.models import Player

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=15, default='', unique=True)
    description = models.CharField(max_length=250)
    created = models.DateTimeField('Creation date')
    def __str__(self):
        return self.name

class GameResult(models.Model):
    #If null, game was tied
    winner = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # 1 - Resolved
    # 2 - Tie
    # 3 - Unfinished
    result = models.IntegerField(default=3)
    start = models.DateTimeField('Game start date')
    end = models.DateTimeField('Game end date')

class GameResultDetail(models.Model):
    result = models.ForeignKey(GameResult, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)