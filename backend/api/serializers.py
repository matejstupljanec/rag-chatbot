from rest_framework import serializers

from .models import Conversation, Message


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class MessageSerializer(serializers.ModelSerializer):
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
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "answer",
            "answered_at",
            "failed_at",
            "sources",
            "created_at",
            "updated_at",
        ]
