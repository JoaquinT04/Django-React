from django.db import models
from author.models import Author
# Create your models here.
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=100)
    # Author of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # ISBN of the book
    isbn = models.CharField(max_length=13)
    # Genre of the book
    genre = models.CharField(max_length=50)
    # Synopsis of the book
    synopsis = models.TextField()
    # Availability status of the book
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title