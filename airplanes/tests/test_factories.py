import random

from django.test import TestCase

from airplanes.constants import AIRPLANE_MIN_ID, AIRPLANE_MAX_ID
from airplanes.models import Airplane
from airplanes.tests.factories import AirplaneFactory


class AirplaneFactoryTestCase(TestCase):
    def test_available_airplane_ids_without_existing_airplanes(self):
        factory = AirplaneFactory()
        count_available_airplane_ids = AIRPLANE_MAX_ID - AIRPLANE_MIN_ID
        available_airplane_ids = factory.available_airplane_ids()
        self.assertEqual(
            len(available_airplane_ids), count_available_airplane_ids
        )

    def test_available_airplane_ids_with_existing_airplanes(self):
        Airplane.objects.create(id=4, number_of_passengers=140)
        Airplane.objects.create(id=5, number_of_passengers=150)
        factory = AirplaneFactory()

        available_airplane_ids = factory.available_airplane_ids()
        count_available_airplane_ids = AIRPLANE_MAX_ID - AIRPLANE_MIN_ID - 2
        self.assertEqual(
            len(available_airplane_ids), count_available_airplane_ids
        )
        self.assertNotIn(4, available_airplane_ids)
        self.assertNotIn(5, available_airplane_ids)

    def test_generate_data_number_of_passenger_provided(self):
        factory = AirplaneFactory()
        data = factory.generate_data(9,99)
        self.assertEqual(data["id"], 9)
        self.assertEqual(data["number_of_passengers"], 99)

    def test_generate_data_without_number_of_passenger_provided(self):
        factory = AirplaneFactory()
        data = factory.generate_data(8)
        self.assertEqual(data["id"], 8)
        self.assertGreaterEqual(data["number_of_passengers"], 0)
        self.assertLessEqual(data["number_of_passengers"], 999)

    def test_get_bulk_data(self):
        # Mocking random.sample to return fixed values
        def sample(population, k):
            return [5]

        random.sample = sample

        factory = AirplaneFactory()
        bulk_data = factory.get_bulk_data(1)
        self.assertEqual(len(bulk_data), 1)
        self.assertEqual(bulk_data[0]["id"], 5)
        self.assertGreaterEqual(bulk_data[0]["number_of_passengers"], 0)
        self.assertLessEqual(bulk_data[0]["number_of_passengers"], 999)
