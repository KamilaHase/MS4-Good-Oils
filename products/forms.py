from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Brand


class ProductForm(forms.ModelForm):
    """ Form for Product model """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-2'

        brands = Brand.objects.all()
        brand_frnames = [(c.id, c.get_brand_frname()) for c in brands]
        self.fields['brand'].choices = brand_frnames
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-2'
