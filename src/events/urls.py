
from django.urls import path

from .views import EventListView

urlpatterns = [
    path("api/events/", EventListView.as_view(), name="event-list"),
]
