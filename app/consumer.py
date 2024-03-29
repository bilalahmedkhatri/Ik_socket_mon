from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import os
import json

from .models import MonitorRomeModel, MonitorMessage


class VideoMonitorConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room = None

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        self.room = MonitorRomeModel.objects.get(name=self.room_name)

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name,)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.layer_discard)(
            self.room_group_name, self.channel_layer,)

    def receive(self, text_data=None, bytes_data=None):
        text_json_data = json.loads(text_data)
        message = text_json_data['message']

        async_to_sync(self.channel_layer.group_sen)(
            self.room_group_name, {"type": "chat", "message": message, })

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))
