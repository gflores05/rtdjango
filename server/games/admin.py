from django.contrib import admin

# Register your models here.
from .models import Game, GameResult, GameResultDetail

admin.site.register(Game)
admin.site.register(GameResult)
admin.site.register(GameResultDetail)
