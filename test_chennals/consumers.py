# chat/consumers.py
import json
import numpy as np
import cv2
import asyncio
import base64
import mss
import random

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        # text_data_json = json.loads(self.scope['url_route']['kwargs'])
        # print('Received ', text_data_json)
        # recv = f"received message from websockets is: {text_data_json}"
        # await self.send(recv)
        # message = text_data.replace('websockets', 'server')
        # print('Received ', self.websocket_receive(text_data))
        print('Received ', type(text_data))

        # text_data.shot(out_put=f"name_{random.randint(100,222)}.png")
    async def websocket_receive(self, message):
        recv = message
        print('recv ', recv)

    async def disconnect(self, close_code):
        pass

# TypeError: AsyncWebsocketConsumer.websocket_receive() missing 1 required positional argument: 'message'

# ['__annotations__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_sync', 'accept', 'as_asgi', 'base_send', 'channel_layer', 'channel_layer_alias', 'close', 'connect', 'disconnect', 'dispatch', 'groups', 'receive', 'scope', 'send', 'websocket_connect', 'websocket_disconnect', 'websocket_receive']
