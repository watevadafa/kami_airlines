from django.conf import settings
from django.test import TestCase

from airplanes.models import Airplane
from airplanes.utils import get_log


class AirplaneTestCase(TestCase):
    def setUp(self):
        self.airplane_1_id = 2
        self.airplane_1_fuel_tank_capacity_in_liters = (
            settings.FUEL_TANK_CAPACITY_MULTIPLIER * self.airplane_1_id
        )
        self.fuel_consumption_rate_per_minute = (
            settings.AIRPLANE_FUEL_CONSUMPTION_MULTIPLIER
            * get_log(self.airplane_1_id)
        )

    def test_airplane_creation(self):
        airplane = Airplane.objects.create(id=self.airplane_1_id)
        self.assertEqual(airplane.id, self.airplane_1_id)
        self.assertEqual(
            airplane.fuel_tank_capacity_in_liters,
            self.airplane_1_fuel_tank_capacity_in_liters,
        )
        self.assertEqual(
            airplane.fuel_consumption_rate_per_minute,
            self.fuel_consumption_rate_per_minute,
        )
