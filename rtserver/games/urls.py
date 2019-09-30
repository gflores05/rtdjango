from django.conf.urls import url, include
from django.urls import path
from games.views import GameViewSet
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'games', GameViewSet)

game_list = GameViewSet.as_view({
    'get': 'list'
})
game_detail = GameViewSet.as_view({
    'get': 'retrieve'
})
game_start = GameViewSet.as_view({
    'post': 'start'
})
urlpatterns = [
    path('games/', game_list, name='game-list'),
    path('games/<int:pk>/', game_detail, name='game-detail'),
    path('game/start/', game_start, name='game-start')
]