# chat/consumers.py
import json
import numpy as np
import cv2
import asyncio
import base64

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        # text_data_json = json.loads(self.scope['url_route']['kwargs'])
        # print('Received ', text_data_json)
        # recv = f"received message from websockets is: {text_data_json}"
        # await self.send(recv)
        message = text_data.replace('websockets', 'server')
        await self.send(message)
        print('Received ', text_data)
        # print('results of ', text_data)

    async def disconnect(self, close_code):
        pass
