from django.db import models


# Create your models here.
class BookStore(models.Model):
    class Meta:
        verbose_name = "Book Store"
        verbose_name_plural = "Book Store"
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=100)
    year_published = models.IntegerField()

