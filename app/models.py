from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MonitorRomeModel(models.Model):
    name = models.CharField(max_length=255)
    online = models.ManyToManyField(User, blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self):
        self.online.add(self.name)
        self.save()

    def leave(self):
        self.online.remove(self.name)
        self.save()

    def __str__(self):
        return f"{self.name} ({self.get_online_count()})"


class MonitorMessage(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monitor = models.ForeignKey(MonitorRomeModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} :- {self.content} [{self.timestamp}]"
