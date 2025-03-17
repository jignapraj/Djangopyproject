# Author: Jigansha Prajpati
from django.contrib import admin
from .models import Inventory

class InventoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Inventory model to display book information in a list format.

    Attributes:
        list_display (tuple): Fields to display in the list view in the admin interface.
        search_fields (tuple): Fields to include in the search bar for filtering results.
        list_filter (tuple): Fields to use for filtering options in the list view.
    """
    list_display = ('title', 'author', 'genre', 'publication_date', 'isbn')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('genre', 'publication_date')

# Register the model with the custom admin configuration
admin.site.register(Inventory, InventoryAdmin)