from rest_framework import serializers

from airplanes.models import Airplane


class AirplaneModelSerializer(serializers.ModelSerializer):
    class Meta:
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
