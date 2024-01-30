from django.shortcuts import render

# Create your views here.
from .models import MonitorRomeModel, MonitorMessage


def index_view(request):
    return render(request, 'index.html', {"rooms": MonitorRomeModel.objects.all()})


def monitor_view(request, room_name):
    monitor, created = MonitorRomeModel.objects.get_or_create(name=room_name)
    return render(request, 'room.html', {"room": monitor})
