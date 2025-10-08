from django.db import models
from django.urls import reverse

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('tecnologia', 'Tecnología'),
        ('hogar', 'Hogar'),
        ('ropa', 'Ropa'),
        ('alimentos', 'Alimentos'),
        ('otros', 'Otros'),
    ]

    name = models.CharField("Nombre", max_length=200)
    description = models.TextField("Descripción Producto", blank=True)   # como lo tenías
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)
    category = models.CharField("Categoría", max_length=50, choices=CATEGORY_CHOICES, default='otros')
    created_at = models.DateTimeField(auto_now_add=True)  # <-- lo agregamos de nuevo

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product-detail', args=[str(self.id)])
