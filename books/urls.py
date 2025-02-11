from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Maps to book_list view
    path('raw-html/', views.rawhtml, name='rawhtml'),
    # path('contactus/', views.contactus, name='contactus'),
]
