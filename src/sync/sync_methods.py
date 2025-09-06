from datetime import datetime

import requests
from django.utils import timezone

from events.models import Event, Platform
from sync.models import SynchronizationResult


def process_event(event):
    event_id = event.get("id")

    event_data = {
        "title": event.get("name"),
        "date_of_event": event.get("event_time"),
        "status": event.get("status"),
        "updated_at": event.get("changed_at"),
    }

    platform_id = event.get("place", {}).get("id")
    platform_name = event.get("place", {}).get("name")

    platform_instance, _ = Platform.objects.get_or_create(
        id=platform_id, defaults={"name": platform_name}
    )

    return event_id, event_data, platform_instance


def sync_events(url, headers, date_filter=None):
    new_events_count = 0
    updated_events_count = 0

    while url:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return f"Ошибка запроса: {str(e)}"

        data = response.json()

        for event in data["results"]:
            if date_filter:
                event_time = datetime.fromisoformat(event["event_time"])
                event_date_str = str(event_time.date())

                if event_date_str != date_filter:
                    continue

            event_id, event_data, platform_instance = process_event(event)

            event_instance, created = Event.objects.update_or_create(
                id=event_id, defaults={**event_data, "platform": platform_instance}
            )

            if created:
                new_events_count += 1
            else:
                updated_events_count += 1

        url = data.get("next")

    SynchronizationResult.objects.create(
        sync_date=timezone.now(),
        new_events_count=new_events_count,
        updated_events_count=updated_events_count,
    )

    return "Синхронизация завершена: {} новых ивентов, {} обновлено.".format(
        new_events_count, updated_events_count
    )
