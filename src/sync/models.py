from django.db import models
from django.utils import timezone


class SynchronizationResult(models.Model):
    sync_date = models.DateTimeField(
        default=timezone.now, verbose_name="Дата синхронизации"
    )
    new_events_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество новых ивентов"
    )
    updated_events_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество обновленных ивентов"
    )

    def __str__(self):
        return f"Синхронизация {self.sync_date.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        verbose_name = "Результат синхронизации"
        verbose_name_plural = "Результаты синхронизации"
