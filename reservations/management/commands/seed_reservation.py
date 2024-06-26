from typing import Any
import random
from datetime import timedelta, datetime
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from reservations import models as reservation_models
from users import models as user_models
from rooms import models as room_models

NAME = "reservations"


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number", default=2, type=int, help=f"How many {NAME} you want to create?"
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()[4:10]

        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()+timedelta(
                    days=random.randint(3, 25)
                    )
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))
