from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from players.models import Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['name', 'nickname', 'level', 'points']

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]