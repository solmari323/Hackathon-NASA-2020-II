import json

from django.test import TestCase
from django.urls import reverse

from .models import Program
from .serializers import ProgramSerializer

from rest_framework import status
from rest_framework.test import APIClient


class GetProgramsTestCase(TestCase):

    client = APIClient()

    def setUp(self):
        Program.objects.create(
            title="Space Mission Alpha",
        )
        Program.objects.create(
            title="Mission 2: Electric Boogaloo",
        )
        Program.objects.create(
            title="Space: Episode III - Revenge of the Sith",
        )

    def test_get_programs(self):
        """
        Test that the user-list route returns a list of programs.
        """
        # Setup.
        url = reverse("program-list")
        # Run.
        response = self.client.get(url, format="json")
        # Check.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                {
                    "url": "http://testserver/api/programs/1/",
                    "id": 1,
                    "title": "Space Mission Alpha",
                },
                {
                    "url": "http://testserver/api/programs/2/",
                    "id": 2,
                    "title": "Mission 2: Electric Boogaloo",
                },
                {
                    "url": "http://testserver/api/programs/3/",
                    "id": 3,
                    "title": "Space: Episode III - Revenge of the Sith",
                },
            ],
        )
