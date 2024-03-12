from django.conf import settings
from django.db import models

from airplanes.utils import get_log


class Airplane(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    fuel_tank_capacity_in_liters = models.PositiveIntegerField()
    fuel_consumption_rate = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Airplane - {self.id}"

    def save(self, *args, **kwargs):
        self.fuel_tank_capacity_in_liters = (
            settings.FUEL_TANK_CAPACITY_MULTIPLIER * self.id
        )
        self.fuel_consumption_rate = (
            settings.AIRPLANE_FUEL_CONSUMPTION_MULTIPLIER * get_log(self.id)
        )
        super(Airplane, self).save(*args, **kwargs)
