from django.db import models


class Page(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(null=True, blank=True)
    scraped_at = models.DateTimeField(null=True, blank=True)
    failed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pages"
        ordering = ["id"]
