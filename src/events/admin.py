from django.contrib import admin

from .models import Event, Platform

# Register your models here.


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_of_event", "status", "platform")
    list_filter = ("status", "platform")
    search_fields = ("title",)
    ordering = ("-date_of_event",)
