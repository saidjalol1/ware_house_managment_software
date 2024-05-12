from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    size = models.CharField(max_length=250)
    paint = models.CharField(max_length=100)
    extra = models.CharField(max_length=100, blank=True, null=True)
    count = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=100, null=True,blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    
    class Meta:
        ordering = ["-date_added"]
    
    
    def get_overall_price(self):
        return self.count * self.price
    
    
    def __str__(self):
        return self.category.name
    
