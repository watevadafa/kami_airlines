from django.test import TestCase

from airplanes.utils import (
    calculate_fuel_tank_capacity_in_liters,
    calculate_fuel_consumption_rate_per_minute,
    calculate_maximum_flight_duration_in_minutes,
)


from airplanes.models import Airplane
from airplanes.tests.factories import AirplaneFactory


class AirplaneModelTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = AirplaneFactory()
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

        self.airplane = Airplane.objects.create(**self.data)

    def test_airplane_creation(self) -> None:
        """Tests if airplane is created successfully"""

        self.assertEqual(self.airplane.id, self.airplane_id)
        self.assertEqual(Airplane.objects.count(), 1)

    def test_airplane_str(self) -> None:
        self.assertEqual(str(self.airplane), self.airplane_str)

    def test_airplane_fuel_tank_capacity_in_liters(self) -> None:
        self.assertEqual(
            self.airplane.fuel_tank_capacity_in_liters,
            self.fuel_tank_capacity_in_liters,
        )

    def test_airplane_fuel_consumption_rate_per_minute(self) -> None:
        self.assertEqual(
            self.airplane.fuel_consumption_rate_per_minute,
            self.fuel_consumption_rate_per_minute,
        )

    def test_airplane_maximum_flight_duration_in_minutes(self) -> None:
        self.assertEqual(
            self.airplane.maximum_flight_duration_in_minutes,
            self.maximum_flight_duration_in_minutes,
        )
