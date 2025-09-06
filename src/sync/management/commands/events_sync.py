from datetime import datetime

from django.core.management.base import BaseCommand

from events.models import Event
from src.sync import sync_methods


class Command(BaseCommand):
    help = "Синхронизировать события с events-provider"

    def add_arguments(self, parser):
        parser.add_argument(
            "--date",
            type=str,
            help="Дата для получения событий в формате YYYY-MM-DD",
        )
        parser.add_argument(
            "--all", action="store_true", help="Синхронизировать все события"
        )

    def handle(self, *args, **kwargs):
        date_param = kwargs["date"]
        all_events = kwargs["all"]

        url = "https://events.k3scluster.tech/api/events/"

        headers = {
            "Authorization": "Bearer <YOUR TOKEN HERE>",
            "Content-Type": "application/json",
        }

        if date_param:
            return sync_methods.sync_events(url, headers, date_param)
        if all_events:
            return sync_methods.sync_events(url, headers)
        else:
            last_event = Event.objects.order_by("-updated_at").first()
            if last_event:
                date_param = datetime.fromisoformat(str(last_event.updated_at))
                date_param = str(date_param.date())
                url = f"https://events.k3scluster.tech/api/events/?changed_at={date_param}"
                return sync_methods.sync_events(url, headers)
            else:
                self.stdout.write("Нет синхронизированных событий для получения даты.")
