from django.db import models
from warehouse.models import Product


class Sale(models.Model):
    customer_name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    quantity = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=200, null=True, blank=True)
    extra = models.CharField(max_length=100)
    deadline = models.DateField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_added"]
    
    def sum_(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return self.customer_name
