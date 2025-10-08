from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm   # 👈  NUEVA IMPORTACIÓN

class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm        # 👈  usar el formulario personalizado
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product-list')  # redirige después de guardar

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm        # 👈  usar el mismo formulario
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy('catalog:product-list')
