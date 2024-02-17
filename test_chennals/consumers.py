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
        await self.accept()

    async def receive(self, text_data):
        # Send the image data to the client
        json_data = await json.loads(text_data)
        print("receive: ", json_data)

    async def disconnect(self, close_code):
        pass
