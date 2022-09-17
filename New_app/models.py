from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name




class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=0)  # 1 to 1
    def __str__(self):
        return self.name
class Сashier(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default= 0)# 1 to 1
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, default=0)
    def __str__(self):
        return self.name
# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    def __str__(self):
        return self.name
