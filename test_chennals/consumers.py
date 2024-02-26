import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None):
        text_data_json = json.dumps(text_data)
        # message = text_data_json[0]
        print("message", text_data_json)
        for x in range(10):
            await self.send(text_data=f"check test {x}")

    async def disconnect(self, close_code):
        pass
