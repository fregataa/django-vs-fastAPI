from django.urls import path

from . import views

urlpatterns = [
    # /testapp/
    path("", views.index, name="index"),
    path("books/", views.list_or_create_book),
    path("books/<int:pk>/", views.get_book),
    path("async-books/", views.async_list_or_create_book),
    path("async-books/<int:pk>/", views.async_get_book),
]
