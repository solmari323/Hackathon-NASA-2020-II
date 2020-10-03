import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .serializers import UserSerializer

from rest_framework import status
from rest_framework.test import APIClient


class GetUsersTestCase(TestCase):

    client = APIClient()

    def setUp(self):
        User = get_user_model()
        User.objects.create(
            username="casperBD",
            first_name="Casper",
            last_name="Bull Dog",
            email="black@dogs.co.uk",
        )
        User.objects.create(
            username="muffinG",
            first_name="Muffin",
            last_name="Gradane",
            email="brown@dogs.co.uk",
        )
        User.objects.create(
            username="ramboL",
            first_name="Rambo",
            last_name="Labrador",
            email="black@dogs.co.uk",
        )

    def test_get_users(self):
        """
        Test that the user-list route returns a list of users.
        """
        # Setup.
        url = reverse("user-list")
        # Run.
        response = self.client.get(url, format="json")
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                {
                    "url": "http://testserver/api/users/1/",
                    "id": 1,
                    "username": "casperBD",
                    "first_name": "Casper",
                    "last_name": "Bull Dog",
                    "email": "black@dogs.co.uk",
                },
                {
                    "url": "http://testserver/api/users/2/",
                    "id": 2,
                    "username": "muffinG",
                    "first_name": "Muffin",
                    "last_name": "Gradane",
                    "email": "brown@dogs.co.uk",
                },
                {
                    "url": "http://testserver/api/users/3/",
                    "id": 3,
                    "username": "ramboL",
                    "first_name": "Rambo",
                    "last_name": "Labrador",
                    "email": "black@dogs.co.uk",
                },
            ],
        )
