from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from airplanes.models import Airplane
from airplanes.serializers import AirplaneSerializer


class AirplaneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @action(detail=False, methods=["post"])
    def evaluate(self, request):
        """
        Accepts bulk data in the form of a list of dict with keys "id" and "number_of_passengers"
        Returns a list of dict with keys "id", "fuel_consumption_rate_per_minute", "maximum_flight_duration_in_minutes"
        """
        serializer = AirplaneSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        instances = []
        for data in request.data:
            instance, updated = Airplane.objects.update_or_create(
                id=data["id"],
                defaults={"number_of_passengers": data["number_of_passengers"]},
            )
            instances.append(instance)

        response_data = AirplaneSerializer(instances, many=True).data
        return Response(response_data)
