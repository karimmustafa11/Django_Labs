from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=50)

    def clean(self):
        if len(self.name) < 2:
            raise ValidationError("Category name must be at least 2 characters long")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def clean(self):
        if not (10 <= len(self.title) <= 50):
            raise ValidationError("Title must be between 10 and 50 characters")

    def __str__(self):
        return self.title

class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    author_title = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.isbn_number