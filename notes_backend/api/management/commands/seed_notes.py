from django.core.management.base import BaseCommand
from django.utils import timezone

from api.models import Note


class Command(BaseCommand):
    help = "Seed the database with sample notes for quick testing."

    # PUBLIC_INTERFACE
    def handle(self, *args, **options):
        """Create a few sample notes if none exist."""
        if Note.objects.exists():
            self.stdout.write(self.style.WARNING("Notes already exist. Skipping seed."))
            return

        now = timezone.now()
        samples = [
            {
                "title": "Welcome to Simple Notes",
                "content": "This is your first note. Feel free to edit or delete it.",
            },
            {
                "title": "Django Tips",
                "content": "Use the Django Rest Framework for quick APIs. Pagination via PageNumberPagination.",
            },
            {
                "title": "Todo",
                "content": "- Add search\n- Add ordering\n- Add pagination\nDone!",
            },
        ]
        for s in samples:
            Note.objects.create(**s)

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(samples)} notes at {now:%Y-%m-%d %H:%M:%S}."))
