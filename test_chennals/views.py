from django.shortcuts import render

# Create your views here.


def video(request, room_name):
    return render(request, "video.html", {"video": room_name})
