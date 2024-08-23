from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Product')
    descript = models.TextField()
    price = models.FloatField()
    sale = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    delivery_adress = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)