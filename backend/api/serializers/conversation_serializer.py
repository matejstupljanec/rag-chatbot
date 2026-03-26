from rest_framework import serializers

from ..models import Conversation


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
