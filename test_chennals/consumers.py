# chat/consumers.py
import json
# import numpy as np
# import cv2
# import asyncio
# import base64
# import mss
# import random

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.channel_layer.
        await self.accept()

    async def receive(self, text_data):
        # Send the image data to the client
        json_data = json.loads(text_data)
        print(json_data['frames'])
        await self.send('send SS from ser dj')

    async def disconnect(self, close_code):
        pass

    async def send_video(self, event):
        video_data = event['video_data']
        await self.send(text_data=json.dumps({'video_data': video_data}))
