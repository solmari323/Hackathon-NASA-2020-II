from django.urls import path, include

from rest_framework import routers

from .viewsets import ScheduleViewSet


# Take care when naming API routes.
# https://restfulapi.net/resource-naming/
router = routers.DefaultRouter()
router.register(r"schedules", ScheduleViewSet)

urlpatterns = []
