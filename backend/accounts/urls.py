from django.urls import path, include

from rest_framework import routers

from .viewsets import UserViewSet


# Take care when naming API routes.
# https://restfulapi.net/resource-naming/
router = routers.DefaultRouter()
router.register(r"accounts/users", UserViewSet)

urlpatterns = []
