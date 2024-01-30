"""
ASGI config for monitor_setting project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

# from app.routing import websocket_urlpatterns
# from test_chennals.routing import websocket_urlpatterns
import test_chennals.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitor_setting.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            test_chennals.routing.websocket_urlpatterns
        )
    ),
    # "websocket": AllowedHostsOriginValidator(websocket_urlpatterns),
})
