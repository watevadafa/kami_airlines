from django.urls import resolve, reverse

from rest_framework.test import APITestCase, APIClient

from airplanes.views import AirplaneViewSet
from airplanes.models import Airplane
from airplanes.tests.factories import AirplaneFactory


class AirplaneViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = AirplaneFactory()
        self.bulk_data: list = self.factory.get_bulk_data(10)
        self.client = APIClient()

        self.view = AirplaneViewSet.as_view({"post": "evaluate"})

    def test_url(self):
        url_name = "airplane-list"
        url_path = "/api/v1/airplanes/"
        self.assertEqual(reverse(url_name), url_path)
        self.assertEqual(resolve(url_path).view_name, url_name)

    def test_airplane_list(self):
        url = reverse("airplane-list")
        Airplane.objects.create(id=999, number_of_passengers=100)
        Airplane.objects.create(id=998, number_of_passengers=1010)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], 999)
        self.assertEqual(response.data[0]["number_of_passengers"], 100)
        self.assertEqual(response.data[1]["id"], 998)
        self.assertEqual(response.data[1]["number_of_passengers"], 1010)

    def test_airplane_evaluate(self):
        url = reverse("airplane-evaluate")
        response = self.client.post(url, self.bulk_data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 10)
