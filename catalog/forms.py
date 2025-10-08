from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Agrega una descripción del producto...',
            }),
            'category': forms.Select(attrs={'class': 'select'}),
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nombre del producto'}),
            'price': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Precio del producto'}),
        }
