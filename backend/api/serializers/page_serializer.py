from rest_framework import serializers

from ..models import Page


class PageSerializer(serializers.ModelSerializer):
    url = serializers.URLField(required=True, allow_blank=False)

    class Meta:
        model = Page
        fields = "__all__"
        read_only_fields = [
            "id",
            "title",
            "scraped_at",
            "failed_at",
            "created_at",
            "updated_at",
        ]
