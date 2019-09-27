from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50, unique=True)
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    created = models.DateTimeField('Creation date')
