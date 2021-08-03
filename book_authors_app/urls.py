from django.urls import path, include
from .views import *

urlpatterns = [
    path('books', books),
    path('books/create', create_book),
    path('books/<int:id>', one_book),
    path('books/<int:id>/delete', delete_book),
    path('books/<int:id>/edit', one_book),
    path('books/add_author', add_author),
    path('authors', authors),
    path('authors/create', create_author),
]