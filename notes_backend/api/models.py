from django.db import models


class Note(models.Model):
    """
    Represents a simple text note with title and content.
    Includes created/updated timestamps for ordering and auditing.
    """
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        ordering = ["-updated_at"]
        indexes = [
            models.Index(fields=["updated_at"]),
            models.Index(fields=["title"]),
        ]

    def __str__(self) -> str:
        return f"{self.title} ({self.updated_at:%Y-%m-%d %H:%M:%S})"
