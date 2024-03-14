from django.core.validators import MaxValueValidator, MinValueValidator

from rest_framework import serializers

from airplanes.constants import AIRPLANE_MIN_ID, AIRPLANE_MAX_ID
from airplanes.models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    """
    Basic Model Serializer for the Airplane model
    """

    id = serializers.IntegerField(
        required=True,
        validators=[
            MinValueValidator(AIRPLANE_MIN_ID),
            MaxValueValidator(AIRPLANE_MAX_ID),
        ],
    )

    class Meta:
        """
        Metadata for the serializer
        """

        model = Airplane
        fields = [
            "id",
            "number_of_passengers",
            "fuel_consumption_rate_per_minute",
            "maximum_flight_duration_in_minutes",
        ]
        read_only_fields = [
            "fuel_consumption_rate_per_minute",
            "maximum_flight_duration_in_minutes",
        ]
