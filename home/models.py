from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField(default=18)
    email=models.EmailField()
    address=models.TextField()
    
class Product(models.Model):
    pass

class Car(models.Model):
    car_name=models.CharField(max_length=30)
    speed=models.IntegerField()

    def __str__(self) -> str:
        return self.car_name
    