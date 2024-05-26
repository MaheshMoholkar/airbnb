from typing import Any
from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any) -> str | None:
        facilities = [
            "Private Entrance",
            "Paid Parking On Premises",
            "Paid Parking Off Premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
