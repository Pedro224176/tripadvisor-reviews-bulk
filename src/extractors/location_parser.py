thonpython
import logging
import random

class LocationParser:
    """
    Simulated parser for Tripadvisor location metadata.
    """

    def get_location_metadata(self, url: str):
        logging.info(f"Simulating location metadata extraction for {url}")

        return {
            "locationId": random.randint(100000, 999999),
            "name": "Sample Location",
            "country": "Sample Country",
            "category": "Hotel"
        }