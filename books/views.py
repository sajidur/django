from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from books.serializers import BookSerializer
# Create your views here.
from .models import Books

def book_list(request):
    books = Books.objects.all()  # Fetch all books from the database
    return render(request, 'books/book_list.html', {'books': books})
def rawhtml(request):
    books = Books.objects.all()  # Fetch all books from the database
    #return render(request, 'books/book_list.html', {'books': books})
    return HttpResponse("test")
    
def contactus(request):
    books = Books.objects.all()  # Fetch all books from the database
    #return render(request, 'books/book_list.html', {'books': books})
    return HttpResponse("test")
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
