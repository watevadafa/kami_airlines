from django.test import TestCase

from airplanes.utils import (
    calculate_fuel_tank_capacity_in_liters,
    calculate_fuel_consumption_rate_per_minute,
    calculate_maximum_flight_duration_in_minutes,
)


from airplanes.models import Airplane
from airplanes.serializers import AirplaneSerializer
from airplanes.tests.factories import AirplaneFactory


class AirplaneSerializerTestCase(TestCase):
    def setUp(self):
        self.factory = AirplaneFactory()
        self.serializer = AirplaneSerializer
        self.data: dict = self.factory.get_data()
        self.airplane_id: int = self.data["id"]
        self.number_of_passengers: int = self.data["number_of_passengers"]
        self.airplane_str: str = f"Airplane - {self.airplane_id}"
        self.fuel_tank_capacity_in_liters: int = (
            calculate_fuel_tank_capacity_in_liters(self.airplane_id)
        )
        self.fuel_consumption_rate_per_minute: float = (
            calculate_fuel_consumption_rate_per_minute(
                self.airplane_id, self.number_of_passengers
            )
        )
        self.maximum_flight_duration_in_minutes: float = (
            calculate_maximum_flight_duration_in_minutes(
                self.fuel_tank_capacity_in_liters,
                self.fuel_consumption_rate_per_minute,
            )
        )

    def test_serializer_save(self):
        # When
        serializer = self.serializer(data=self.data)
        is_valid = serializer.is_valid(raise_exception=True)
        airplane = serializer.save()

        # Then
        self.assertTrue(is_valid)
        self.assertEqual(airplane.id, self.airplane_id)
        self.assertEqual(Airplane.objects.count(), 1)
        self.assertEqual(str(airplane), self.airplane_str)

    def test_valid_id_field_validators(self):
        # Test valid id value
        valid_data = {
            "id": 345,
            "number_of_passengers": 345,
        }
        serializer = self.serializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["id"], 345)
        self.assertEqual(serializer.validated_data["number_of_passengers"], 345)

    def test_invalid_id_field_validators_min(self):
        invalid_data_min = {
            "id": 0,
            "number_of_passengers": 345,
        }
        serializer = self.serializer(data=invalid_data_min)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["id"][0],
            "Ensure this value is greater than or equal to 1.",
        )

    def test_invalid_id_field_validators_max(self):
        invalid_data_max = {
            "id": 10000,
            "number_of_passengers": 345,
        }
        serializer = self.serializer(data=invalid_data_max)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["id"][0],
            "Ensure this value is less than or equal to 9999.",
        )
