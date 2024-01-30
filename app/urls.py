from django.urls import path
from .views import index_view, monitor_view


urlpatterns = [
    path("", index_view, name="index"),
    path("<str:room_name>", monitor_view, name="room"),
]
