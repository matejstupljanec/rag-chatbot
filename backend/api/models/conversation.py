from django.db import models
from .user import User


class Conversation(models.Model):
    name = models.CharField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="conversations",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "conversations"
        ordering = ["-id"]
