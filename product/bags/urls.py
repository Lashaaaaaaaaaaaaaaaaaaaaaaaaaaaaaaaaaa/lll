from django.urls import path
from .views import (ProductListCreate, ProductRetrieveUpdateDestroy, ProductDelete, CategoryListCreate, CategoryRetrieveUpdateDestroy,
                    CategoryDelete)

urlpatterns = [
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product-delete'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy'),
    path('categories/<int:pk>/delete/', CategoryDelete.as_view(), name='category-delete'),
]