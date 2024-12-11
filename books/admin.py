from django.contrib import admin

# Register your models here.
from .models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'price')  # Display columns
    search_fields = ('title', 'author')  # Search bar
    list_filter = ('published_date',)  # Sidebar filters

