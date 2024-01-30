from django.urls import re_path

from .consumer import VideoMonitorConsumer


websocket_urlpatterns = [
    re_path(r'ws/monitor/(?P<room_name>\w+)/$',
            VideoMonitorConsumer.as_asgi()),
]
