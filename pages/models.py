from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image =models.ImageField(null=True ,blank=True)
    def __str__(self):
        return self.name

class Car(models.Model):
    name_Car=models.CharField(max_length=50)
    def __str__(self):
        return self.name_Car
class Employee(models.Model):
    username=models.CharField(max_length=50)
    Car=models.OneToOneField(Car,max_length=50,on_delete=models.CASCADE)
    def __str__(self):
        return self.username
class Category(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title
class User(models.Model):
    user=models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.user    
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username
    