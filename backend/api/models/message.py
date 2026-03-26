from django.db import models
from .conversation import Conversation

class Message(models.Model):
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    liked_at = models.DateTimeField(null=True, blank=True)
    disliked_at = models.DateTimeField(null=True, blank=True)
    answered_at = models.DateTimeField(null=True, blank=True)
    failed_at = models.DateTimeField(null=True, blank=True)
    sources = models.JSONField(null=True, blank=True)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "messages"
        ordering = ["id"]
