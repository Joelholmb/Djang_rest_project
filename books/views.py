from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        # Hämta data från formuläret
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')

        # Skapa och spara en ny bok
        Book.objects.create(
            title=title,
            author=author,
            description=description,
            published_date=published_date,
            isbn=isbn
        )
        # Omdirigera till startsidan efter att boken skapats
        return redirect('index')

    # Om GET, rendera formuläret
    return render(request, 'books/create_book.html')

def book_list(request):
    books = Book.objects.all()  # Hämtar alla böcker från databasen
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Hämta boken eller visa 404
    return render(request, 'books/book_detail.html', {'book': book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Hämta boken eller visa 404
    book.delete()  # Radera boken
    return redirect('book-list')  # Omdirigera till boklistan efter radering

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Hämta boken eller visa 404
    if request.method == 'POST':
        # Uppdatera bokens data baserat på formuläret
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.published_date = request.POST.get('published_date')
        book.isbn = request.POST.get('isbn')
        book.save()
        return redirect('book-detail', pk=book.pk)  # Omdirigera till bokdetaljer efter redigering

    # Om GET, rendera formuläret med befintliga värden
    return render(request, 'books/edit_book.html', {'book': book})