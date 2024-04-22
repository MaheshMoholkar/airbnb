from django.db import models
from core import models as core_models


# Create your models here.
class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self) -> str:
        return self.created


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} says: {self.message}"
