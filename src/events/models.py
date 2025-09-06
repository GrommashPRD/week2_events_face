import enum
import uuid
from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class EventStatus(enum.Enum):
    OPEN: str = "OPEN"
    CLOSED: str = "CLOSED"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Platform(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    name = models.CharField(max_length=255, verbose_name="Platform Name")

    def __str__(self):
        return self.name

    class Meta:
        app_label = "events"
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"


class Event(models.Model):
    id: uuid.UUID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title: str = models.CharField(max_length=255, verbose_name="Event Title")
    date_of_event: timezone = models.DateTimeField(
        default=timezone.now, verbose_name="Event Date"
    )
    status: EventStatus = models.CharField(
        max_length=10,
        choices=EventStatus.choices(),
        default=EventStatus.OPEN,
        verbose_name="Event Status",
    )
    platform: Platform = models.ForeignKey(
        Platform,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name="Event Platform",
    )
    updated_at: datetime = models.DateTimeField(
        default=timezone.now, verbose_name="Event Updated"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-date_of_event"]
