from django.db import models

from airplanes.utils import (
    calculate_fuel_tank_capacity_in_liters,
    calculate_fuel_consumption_rate_per_minute,
    calculate_maximum_flight_duration_in_minutes,
)


class Airplane(models.Model):
    """
    Airplane model with fields `id` and the assumed `number_of_passengers`
    Others are calculated properties include
    """

    id = models.PositiveIntegerField(primary_key=True)
    number_of_passengers = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"Airplane - {self.id}"

    @property
    def fuel_tank_capacity_in_liters(self) -> int:
        return calculate_fuel_tank_capacity_in_liters(self.id)

    @property
    def fuel_consumption_rate_per_minute(self) -> float:
        return calculate_fuel_consumption_rate_per_minute(
            self.id, self.number_of_passengers
        )

    @property
    def maximum_flight_duration_in_minutes(self) -> float:
        return calculate_maximum_flight_duration_in_minutes(
            self.fuel_tank_capacity_in_liters,
            self.fuel_consumption_rate_per_minute,
        )
