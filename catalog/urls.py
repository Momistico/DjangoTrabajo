from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/add/', views.ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-edit'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
]
