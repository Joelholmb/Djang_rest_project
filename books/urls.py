from django.urls import path
from .views import index, create_book, book_list, book_detail, delete_book, edit_book

urlpatterns = [
    path('', index, name='index'),  # Startsidan
    path('books/', book_list, name='book-list'),  # Lista alla böcker
    path('books/create/', create_book, name='create-book'),  # Skapa en ny bok
    path('books/<int:pk>/', book_detail, name='book-detail'),  # Visa detaljer om en bok
    path('books/edit/<int:pk>/', edit_book, name='edit-book'),  # Redigera en bok
    path('books/delete/<int:pk>/', delete_book, name='delete-book'),  # Radera en bok
]
