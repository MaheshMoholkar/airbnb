from typing import Any
import random
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from rooms.models import RoomType, Room
from users.models import User


class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create?"
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        room_types = RoomType.objects.all()

        seeder.add_entity(
            Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(0, 10),
                "price": lambda x: random.randint(0, 300),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))
