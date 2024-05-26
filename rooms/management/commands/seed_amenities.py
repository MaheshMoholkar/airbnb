from typing import Any
from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        amenities = [
            "Air Conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon Monoxide Detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double Bed",
            "Free Parking",
            "Free WiFi",
            "Freezer",
            "Golf",
            "Hair Dryer",
            "Hot Tub",
            "Indoor Pool",
            "Ironing Board",
            "Outdoor Tennis",
            "Oven",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke Detectors",
            "Sofa",
            "Stereo",
            "Towels",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} amenities created!"))
