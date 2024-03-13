from rest_framework import serializers

from airplanes.models import Airplane


class AirplaneModelSerializer(serializers.ModelSerializer):
    """
    Basic Model Serializer for the Airplane model
    """

    class Meta:
        """
        Metadata for the serializer
        """

        model = Airplane
        fields = [
            "id",
            "fuel_tank_capacity_in_liters",
            "fuel_consumption_rate_per_minute",
        ]
        read_only_fields = [
            "fuel_tank_capacity_in_liters",
            "fuel_consumption_rate_per_minute",
        ]
