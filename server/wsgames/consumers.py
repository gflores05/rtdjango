from channels.generic.websocket import AsyncWebsocketConsumer
import json


class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_session = self.scope["url_route"]["kwargs"]["game_session"]
        self.room_group_name = "game_%s" % self.game_session

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "game_movement", "data": text_data}
        )

    async def challenge(self, event):
        pass

    async def challenge_accepted(self, event):
        pass

    # Receive message from room group
    async def movement(self, event):
        data = event["data"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"data": data}))
