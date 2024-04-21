from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='assets/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='assets/')

    def __str__(self):
        return self.name