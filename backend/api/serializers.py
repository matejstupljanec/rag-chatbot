from rest_framework import serializers

from .models import Conversation, Message


class ConversationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_blank=False)

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
            "answered_at",
            "failed_at",
            "sources",
            "conversation_idcreated_at",
            "updated_at",
        ]
