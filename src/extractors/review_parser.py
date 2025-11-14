thonpython
import logging
import random
from datetime import datetime

class ReviewParser:
    """
    Simulates extraction of reviews from Tripadvisor.
    Replace with real scraping logic if needed.
    """

    def extract_reviews(self, url: str):
        logging.info(f"Simulating review extraction for {url}")

        fake_reviews = []
        for i in range(3):
            fake_reviews.append({
                "id": random.randint(1000000, 9999999),
                "title": "Sample Review Title",
                "language": "en",
                "text": "This is a simulated review text.",
                "rating": random.randint(1, 5),
                "publishedAt": datetime.now().strftime("%Y-%m-%d"),
                "trip": {
                    "stayDate": datetime.now().strftime("%Y-%m-%d"),
                    "tripType": "COUPLES"
                },
                "url": url,
                "username": f"user_{random.randint(100,999)}",
                "userLocation": {
                    "locationId": random.randint(1000, 9999),
                    "additionalNames": {"long": "Sample City"},
                    "name": "Sample"
                },
                "userCounts": {
                    "sumAllUgc": random.randint(0, 500),
                    "sumAllLikes": random.randint(0, 200)
                },
                "publishedOn": "WEB",
                "labels": []
            })

        return fake_reviews