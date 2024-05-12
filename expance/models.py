from django.db import models


class Expance(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    amount = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_added"]
        
    def __str__(self):
        return self.name