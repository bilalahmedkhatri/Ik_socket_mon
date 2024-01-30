from django.urls import re_path, path
from .consumers import ChatConsumer

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/$', consumers.ChatConsumer.as_asgi()),
    # path(r"/", ChatConsumer.as_asgi()),
]