from django import forms
from .models import Product

# Form for adding and updating products including image uploads
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'image']