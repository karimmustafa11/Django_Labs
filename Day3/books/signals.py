from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, ISBN
import uuid

@receiver(post_save, sender=Book)
def create_isbn_for_book(sender, instance, created, **kwargs):
    if created:
        ISBN.objects.create(
            book=instance,
            author_title=f"Author of {instance.title}",
            book_title=instance.title,
            isbn_number=str(uuid.uuid4())[:13],
        )