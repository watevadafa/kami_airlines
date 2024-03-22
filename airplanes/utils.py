""" Provdies neccessary utility functions for calculating propeties of airplanes"""

import math

from airplanes.constants import (
    FUEL_TANK_CAPACITY_MULTIPLIER,
    AIRPLANE_FUEL_CONSUMPTION_MULTIPLIER,
    PER_PASSENGER_FUEL_CONSUMPTION_MULTIPLIER,
)


def calculate_fuel_tank_capacity_in_liters(airplane_id: int) -> int:
    """Returns the airplane's fuel tank capacity in liters"""
    return airplane_id * FUEL_TANK_CAPACITY_MULTIPLIER


def calculate_fuel_consumption_rate_per_minute(
    airplane_id: int, number_of_passengers: int
) -> float:
    """Returns the airplane's fuel consumption rate in liters per minute"""

    log_of_airplane_id: float = 0 if airplane_id == 0 else math.log(airplane_id)

    airplane_fuel_consumption_per_minute: float = (
        log_of_airplane_id * AIRPLANE_FUEL_CONSUMPTION_MULTIPLIER
    )
    per_passenger_fuel_consumption_per_minute: float = (
        number_of_passengers * PER_PASSENGER_FUEL_CONSUMPTION_MULTIPLIER
    )

    return (
        airplane_fuel_consumption_per_minute
        + per_passenger_fuel_consumption_per_minute
    )


def calculate_maximum_flight_duration_in_minutes(
    fuel_tank_capacity_in_liters: int,
    fuel_consumption_rate_per_minute: float,
) -> float:
    """Returns the maximum flight duration in minutes"""

    return fuel_tank_capacity_in_liters / fuel_consumption_rate_per_minute
