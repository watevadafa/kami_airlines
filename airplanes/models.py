from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from airplanes.constants import (
    AIRPLANE_MIN_ID,
    AIRPLANE_MAX_ID,
    DEFAULT_NUMBER_OF_PASSENGERS,
)
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

    id = models.PositiveIntegerField(
        primary_key=True,
        validators=[
            MinValueValidator(AIRPLANE_MIN_ID),
            MaxValueValidator(AIRPLANE_MAX_ID),
        ],
    )
    number_of_passengers = models.PositiveIntegerField(
        default=DEFAULT_NUMBER_OF_PASSENGERS
    )

    def __str__(self) -> str:
        return f"Airplane - {self.id}"

    @property
    def fuel_tank_capacity_in_liters(self) -> int:
        return calculate_fuel_tank_capacity_in_liters(int(self.id))

    @property
    def fuel_consumption_rate_per_minute(self) -> float:
        return calculate_fuel_consumption_rate_per_minute(
            int(self.id), int(self.number_of_passengers)
        )

    @property
    def maximum_flight_duration_in_minutes(self) -> float:
        return calculate_maximum_flight_duration_in_minutes(
            self.fuel_tank_capacity_in_liters,
            self.fuel_consumption_rate_per_minute,
        )
