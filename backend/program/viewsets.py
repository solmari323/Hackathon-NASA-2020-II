from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Program
from .serializers import ProgramSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing programs.
    """

    queryset = Program.objects.all()

    serializer_class = ProgramSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
