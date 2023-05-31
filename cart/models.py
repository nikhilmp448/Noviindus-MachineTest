from django.db import models
from user.models import Account
from product.models import Product

# Create your models here.

class OrderItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"