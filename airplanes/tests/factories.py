import random

from airplanes.constants import AIRPLANE_MIN_ID, AIRPLANE_MAX_ID
from airplanes.models import Airplane


class AirplaneFactory:
    """
    Factory class to generate test data for Airplane model
    """

    def available_airplane_ids(self) -> list:
        """Returns a list of available airplane ids that can be used to generate test data"""

        airplane_id_range = list(range(AIRPLANE_MIN_ID, AIRPLANE_MAX_ID))

        existing_airplane_ids = list(
            Airplane.objects.all().values_list("id", flat=True)
        )

        available_airplane_ids = list(
            set(airplane_id_range) - set(existing_airplane_ids)
        )

        return available_airplane_ids

    def generate_data(
        self, airplane_id: int, number_of_passengers: int = None
    ) -> dict:
        """Returns a single randomly generated airplane test data dict"""

        data: dict = {}
        data["id"] = airplane_id
        data["number_of_passengers"] = (
            number_of_passengers
            if number_of_passengers
            else random.randint(0, 999)
        )

        return data

    def get_data(self) -> dict:
        """Returns a single randomly generated airplane_id as test data dict"""

        available_airplane_ids = self.available_airplane_ids()
        airplane_id = random.choice(available_airplane_ids)
        return self.generate_data(airplane_id)

    def get_bulk_data(self, count=1) -> list:
        """Returns a list of randomly generated airplane_ids as test data array"""

        available_airplane_ids = self.available_airplane_ids()
        return [
            self.generate_data(id)
            for id in random.sample(available_airplane_ids, count)
        ]
