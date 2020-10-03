from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    User = get_user_model()
    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]
