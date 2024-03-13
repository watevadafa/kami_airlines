from django.conf import settings
from django.db import models

from airplanes.utils import get_log


class Airplane(models.Model):
    """
    Airplane model with only id field.
    fuel_tank_capacity_in_liters and fuel_consumption_rate_per_minute are calculated properties.
    """

    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return f"Airplane - {self.id}"

    @property
    def fuel_tank_capacity_in_liters(self):
        """
        Returns the airplane's fuel tank capacity in liters
        """
        return (
            None
            if self.id is None
            else self.id * settings.FUEL_TANK_CAPACITY_MULTIPLIER
        )

    @property
    def fuel_consumption_rate_per_minute(self):
        """
        Returns the airplane's fuel consumption rate in liters per minute
        """
        return (
            None
            if self.id is None
            else get_log(self.id)
            * settings.AIRPLANE_FUEL_CONSUMPTION_MULTIPLIER
        )
