import random

from django.conf import settings
from django.test import TestCase

from airplanes.constants import AIRPLANE_MIN_ID, AIRPLANE_MAX_ID
from airplanes.models import Airplane
from airplanes.serializers import AirplaneModelSerializer
from airplanes.utils import get_log


class AirplaneFactory:
    """
    Factory class to generate test data for Airplane model
    """

    def available_airplane_ids(self):
        """
        Returns a list of available airplane ids that can be used to generate test data
        """
        airplane_id_range = list(range(AIRPLANE_MIN_ID, AIRPLANE_MAX_ID))

        existing_airplane_ids = list(
            Airplane.objects.all().values_list("id", flat=True)
        )

        available_airplane_ids = list(
            set(airplane_id_range) - set(existing_airplane_ids)
        )

        return available_airplane_ids

    def get_bulk_data(self, count=1):
        """
        Returns a list of randomly generated airplane_ids as test data array
        """
        available_airplane_ids = self.available_airplane_ids()
        data = [
            {"id": id} for id in random.sample(available_airplane_ids, count)
        ]
        return data

    def get_data(self):
        """
        Returns a single randomly generated airplane_id as test data dict
        """

        available_airplane_ids = self.available_airplane_ids()
        data: dict = {"id": random.choice(available_airplane_ids)}
        return data


class AirplaneTestCase(TestCase):
    """
    Tests for Airplane model
    """

    def setUp(self):
        self.data = AirplaneFactory().get_data()
        self.expected_airplane_id = self.data["id"]
        self.expected_airplane_str = f"Airplane - {self.expected_airplane_id}"
        self.expected_airplane_fuel_tank_capacity_in_liters = (
            settings.FUEL_TANK_CAPACITY_MULTIPLIER * self.expected_airplane_id
        )
        self.fuel_consumption_rate_per_minute = (
            settings.AIRPLANE_FUEL_CONSUMPTION_MULTIPLIER
            * get_log(self.expected_airplane_id)
        )

    def test_airplane_creation(self):
        
        airplane = Airplane.objects.create(**self.data)
        self.assertEqual(airplane.id, self.expected_airplane_id)
        self.assertEqual(
            airplane.fuel_tank_capacity_in_liters,
            self.expected_airplane_fuel_tank_capacity_in_liters,
        )
        self.assertEqual(
            airplane.fuel_consumption_rate_per_minute,
            self.fuel_consumption_rate_per_minute,
        )

    def test_airplane_str(self):
        airplane = Airplane.objects.create(id=self.expected_airplane_id)
        expected_str = f"Airplane - {self.expected_airplane_id}"
        self.assertEqual(str(airplane), expected_str)


class AirplaneSerializerTestCase(TestCase):
    def setUp(self):
        self.serializer = AirplaneModelSerializer

    def test_create_airplanes(self):
        data = AirplaneFactory().get_data()
        expected_airplane_id = data["id"]
        expected_airplane_str = f"Airplane - {expected_airplane_id}"

        # When
        serializer = self.serializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        airplane = serializer.save()

        # Then
        self.assertTrue(is_valid)
        self.assertEqual(airplane.id, expected_airplane_id)
        self.assertEqual(str(airplane), expected_airplane_str)
