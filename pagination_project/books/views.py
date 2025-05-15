from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by('title')
    
    # Get items per page from request, default to 5
    items_per_page = request.GET.get('per_page', 5)
    try:
        items_per_page = int(items_per_page)
    except ValueError:
        items_per_page = 5
    
    paginator = Paginator(books, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'books/book_list.html', {
        'page_obj': page_obj,
        'items_per_page': items_per_page
    })