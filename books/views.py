from django.shortcuts import render

# Create your views here.
from .models import Books

def book_list(request):
    books = Books.objects.all()  # Fetch all books from the database
    return render(request, 'books/book_list.html', {'books': books})

