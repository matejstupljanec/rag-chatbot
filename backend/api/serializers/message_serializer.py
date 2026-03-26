from rest_framework import serializers

from ..models import Message


class MessageSerializer(serializers.ModelSerializer):
    question = serializers.CharField(required=True, allow_blank=False)

    class Meta:
        model = Message
        fields = [
            "id",
            "question",
            "answer",
            "liked_at",
            "disliked_at",
            "answered_at",
            "failed_at",
            "sources",
            "conversation_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "answer",
            "liked_at",
            "disliked_at",
            "answered_at",
            "failed_at",
            "sources",
            "conversation_id",
            "created_at",
            "updated_at",
        ]
