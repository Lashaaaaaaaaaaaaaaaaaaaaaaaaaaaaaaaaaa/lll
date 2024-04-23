from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, ProductImage
from .serializers import ProductSerializer, CategorySerializer


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        product = Product.objects.create(**validated_data)

        for image in uploaded_images:
            ProductImage.objects.create(product=product, image=image)

        return product


class CategoryDelete(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer