from django.urls import path
from . import views
from .views import BookListCreateView

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Maps to book_list view
    path('raw-html/', views.rawhtml, name='rawhtml'),
    path('api/', BookListCreateView.as_view(), name='book-list'),

    # path('contactus/', views.contactus, name='contactus'),
]
