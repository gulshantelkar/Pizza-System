from django.db import models
from django.utils import timezone 

class PizzaBase(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return str(self.id)

class Order(models.Model):
    order_date = models.DateTimeField(default=timezone.now())
    customer_name = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    pizzas = models.ManyToManyField(Pizza)
    status = models.CharField(max_length=15, default='Placed')

    def __str__(self):
        return str(self.id)

