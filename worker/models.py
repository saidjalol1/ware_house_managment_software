from django.db import models
from warehouse.models import Category


class Worker(models.Model):
    name = models.CharField(max_length=150, blank=True)
    surname = models.CharField(max_length=150, blank=True)
    type = models.CharField(max_length=100)
    
    account = models.CharField(max_length=100, blank=True)
    salary = models.PositiveBigIntegerField(default=0)
    per_hour = models.PositiveBigIntegerField(default=0)
    
    advance_payment = models.PositiveIntegerField(default=0)
    work_type = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, related_name="workers")
    
    
    def __str__(self):
        return self.name + " " + self.surname


class Attandance(models.Model):
    worker = models.ForeignKey(Worker, related_name="attandances", on_delete=models.CASCADE )
    come = models.TimeField(blank=True, null=True)
    leave = models.TimeField(blank=True, null=True)
    paid = models.PositiveIntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_added"]
    
    def __str__(self):
        return self.worker.name
    
class Payments(models.Model):
    worker = models.ForeignKey(Worker, related_name="payments", on_delete=models.CASCADE )
    amount = models.PositiveBigIntegerField(default=0)
    type = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_added"]
    
    def __str__(self):
        return self.worker.name

class WorkType(models.Model):
    worker = models.ForeignKey(Worker, related_name="payment", on_delete=models.CASCADE )
    work_type = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="payments")
    amount = models.PositiveBigIntegerField(default=0)
    paid = models.PositiveBigIntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ["-date_added"]
    
    def __str__(self):
        return self.worker.name