from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

@login_required
@permission_required('books.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})