from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField("Nombre", max_length=200)
    description = models.TextField("Descripcion Producto",blank=True)
    price = models.DecimalField("Precio",max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product-detail', args=[str(self.id)])
