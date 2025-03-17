# Author: Jigansha Prajpati
from django import forms
from .models import Inventory

class BookForm(forms.ModelForm):
    """
    Form for adding or updating book entries in the inventory.

    Inherits:
        forms.ModelForm: Base class for forms based on Django models.

    Attributes:
        title (CharField): Field for entering the book title.
        author (CharField): Field for entering the author's name.
        genre (CharField): Field for selecting the genre of the book.
        publication_date (DateField): Field for specifying the publication date.
        isbn (BigIntegerField): Field for entering the unique ISBN number.
    """

    class Meta:
        model = Inventory
        fields = ['title', 'author', 'genre', 'publication_date', 'isbn']
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'genre': 'Genre',
            'publication_date': 'Publication Date',
            'isbn': 'ISBN Number'
        }
        help_texts = {
            'title': 'Enter the title of the book.',
            'author': 'Enter the author\'s name.',
            'genre': 'Choose a genre.',
            'publication_date': 'Specify the publication date (optional).',
            'isbn': 'Enter the unique ISBN number of the book.'
        }