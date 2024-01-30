from django.contrib import admin

# Register your models here.
from .models import MonitorRomeModel, MonitorMessage


@admin.register(MonitorRomeModel)
class MonitorRomeModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MonitorMessage)
class MonitorMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'monitor', 'content', 'timestamp')
