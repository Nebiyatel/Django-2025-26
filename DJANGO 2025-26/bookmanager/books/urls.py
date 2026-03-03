from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path("books/create/", views.create_book, name="create_book"),
    path("books/<int:pk>/update/", views.update_book, name="update_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
    path("authors/", views.author_list, name="author_list"),
    path("authors/<int:pk>/", views.author_detail, name="author_detail"),
]
from django.urls import path, include

urlpatterns = [
    path("", include("books.urls")),
]
