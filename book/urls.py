from django.urls import path
from book.views import create_book
urlpatterns = [
    path('book/',create_book),
]
