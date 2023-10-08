from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Equip(models.Model):
    eq_id= models.IntegerField()
    name = models.CharField(max_length=100)
    quantity_available = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equip, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()
    branch = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[("Pending", "Pending"), ("Accepted", "Accepted"), ("Rejected", "Rejected")])
    def __str__(self):
        return f"{self.user.username} - {self.equipment.name}"
