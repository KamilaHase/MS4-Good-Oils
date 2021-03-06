from django import forms
from .models import ProductReview


class ReviewForm(forms.ModelForm):
    """
    Create a form for users to add reviews
    """
    class Meta:
        model = ProductReview
        exclude = (
            'user',
            'date_added',
            'product',
        )

        fields = ['nickname', 'description', 'rating']

        labels = {
            'rating': 'Rating',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'nickname': 'Nickname',
            'description': 'Description',
        }

        """Add placeholders and classes to input fields"""
        self.fields['description'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

            self.fields[field].widget.attrs['class'] = 'add-product-form-field'
