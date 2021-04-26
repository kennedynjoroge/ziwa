from django.shortcuts import render
from .models import BookStore


def home_view(request):
    year_published = BookStore.objects.get(year_published=1975)
    book_author = BookStore.objects.get(book_author="Chinua Achebe")
    return render(request, "home.html", {"year_published": year_published, "book_author": book_author})
