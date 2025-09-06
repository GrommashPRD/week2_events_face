from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Event, EventStatus
from .serializers import EventSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class EventListView(generics.ListAPIView):
    queryset = Event.objects.filter(status="new").select_related(
        "platform"
    )
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["title"]
    filter_set_fields = ["status"]
    permission_classes = [IsAuthenticated]
