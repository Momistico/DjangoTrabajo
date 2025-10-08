from django.db import models
from django.urls import reverse

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Tecnologia', 'Tecnología'),
        ('Hogar', 'Hogar'),
        ('Ropa', 'Ropa'),
        ('Alimentos', 'Alimentos'),
        ('Otros', 'Otros'),
    ]

    name = models.CharField("Nombre", max_length=200)
    description = models.TextField("Descripción Producto", blank=True) 
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    category = models.CharField("Categoría", max_length=50, choices=CATEGORY_CHOICES, default='otros')
    created_at = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product-detail', args=[str(self.id)])
