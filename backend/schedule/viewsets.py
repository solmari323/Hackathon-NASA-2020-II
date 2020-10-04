from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing schedules.
    """

    queryset = Schedule.objects.all()

    serializer_class = ScheduleSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
