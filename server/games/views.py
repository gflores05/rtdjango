from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from players.models import Player
from games.models import Game, GameResultDetail, GameResult  # , GameMovement


# Create your views here.
class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ["code", "name", "description"]


class GameResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GameResult
        fields = ["id", "start"]


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=True, methods=["post"], permission_classes=[AllowAny])
    def start(self, request, pk=None):
        game = Game.objects.get(pk=request.data["game"])
        game_result = game.gameresult_set.create()

        for player_id in request.data["players"]:
            player = Player.objects.get(pk=player_id)
            game_result.gameresultdetail_set.create(player=player)

        return Response(GameResultSerializer(game_result).data)

    @action(detail=True, methods=["post"])
    def movement(self, request, pk=None):
        data = request.data

        # Update player result detail
        if data["points"] > 0:
            result_detail = GameResultDetail.objects.get(
                player=data["player"], result=data["result"]
            )
            result_detail.points += data["points"]
            result_detail.save()

        # Save movement detail
        # movement = GameMovement()
        # movement.detail = result_detail.id
        # movement.points = data["points"]
        # movement.movement = data["movement"]
        # movement.save()

        return Response({"succes": "true"})
