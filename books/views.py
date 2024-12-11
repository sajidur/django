from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Books

def book_list(request):
    books = Books.objects.all()  # Fetch all books from the database
    return render(request, 'books/book_list.html', {'books': books})
def rawhtml(request):
    books = Books.objects.all()  # Fetch all books from the database
    #return render(request, 'books/book_list.html', {'books': books})
    return HttpResponse("test")

