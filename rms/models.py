from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Food(models.Model):
    name=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Table(models.Model):
    name=models.CharField(max_length=250)
    capacity=models.IntegerField(null=True)
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return self.name 
    
class Order(models.Model):
    PENDING = "P"
    IN_PROGRESS = "IP"
    COMPLETED = "CO"
    DELIVERED = "D"
    CANCELLED="CA"
    
    STATUS_CHOICES = {
        PENDING: "Pending",
        IN_PROGRESS: "in progress",
        COMPLETED : "completed",
        DELIVERED: "delivered",
        
    }
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    table=models.ForeignKey(Table,on_delete=models.CASCADE,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=250,choices=STATUS_CHOICES,default=PENDING)
    payment=models.BooleanField(default=False)
    foods=models.ManyToManyField(Food)

    def __str__(self):
        return f"order{self.id} - {self.status}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    food=models.ForeignKey(Food,on_delete=models.PROTECT)

    
    