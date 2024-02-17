from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
    re_path(r'user/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r'ws/$', consumers.ChatConsumer.as_asgi()),
    # re_path(r"^ws/(?P<name_of_user>\w+)/$",
    # consumers.ChatsConsumer.as_asgi()),
    # path(r"/", ChatConsumer.as_asgi()),
]
