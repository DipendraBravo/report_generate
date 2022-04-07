from django.db import models
from products.models import Product
from customers.models import Customer

# Create your models here.

class Position(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"id:{self.id}, product:{self.product.name}, quantity:{self.quantity}"
    

class Sale(models.Model):
    transaction_id = models.CharField(max_length=12, blank=True)
    pass

class CSV(models.Model):
    pass
