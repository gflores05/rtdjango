from django.conf.urls import url, include
from django.contrib.auth.models import User
from players.views import PlayerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"players", PlayerViewSet)

urlpatterns = [
    url(r"^", include(router.urls)),
]
