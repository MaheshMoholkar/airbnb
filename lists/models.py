from django.db import models
from core import models as core_models


# Create your models here.
class List(core_models.TimeStampedModel):
    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self) -> str:
        return self.name

    def count_rooms(self) -> str:
        return self.rooms.count()

    count_rooms.short_description = "No. of Rooms"
