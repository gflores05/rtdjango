from django.db import models
from django.utils import timezone

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50, unique=True)
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    created = models.DateTimeField('Creation date', default=timezone.now())
    def __str__(self):
        return "{0} - {1}".format(self.id, self.name)