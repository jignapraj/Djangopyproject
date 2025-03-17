# Author: Jigansha Prajpati

from django.urls import path
from . import views
from .views import inventory_list, export_inventory_json, delete_book

# App name for URL namespacing
app_name = 'books_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('inventory/', inventory_list, name='inventory_list'),
    path('inventory/export/json/', export_inventory_json, name='export_inventory_json'),
]