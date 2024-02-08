from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/sse$', consumers.ChatConsumer.as_asgi()),
    re_path(r"^ws/(?P<name_of_user>\w+)/$",
            consumers.ChatConsumer.as_asgi()),
    # path(r"/", ChatConsumer.as_asgi()),
]
