from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "url",
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
        ]
