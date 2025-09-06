from rest_framework import serializers

from .models import Event, Platform


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    platform_name = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ("id", "title", "date_of_event", "status", "platform", "platform_name")

    def get_platform_name(self, obj):
        return obj.platform.name if obj.platform else None
