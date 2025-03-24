# models.py
# So here are my models for the car dealership system. 
# These are based on the ERD we got for Part C of the test.

from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        # This makes each Dealer show up by name if we print it or see it in admin.
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        # Same idea here, we’re returning the customer's name in a string.
        return self.name

class Car(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='cars')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    colour = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # Returning a neat identifier for this Car: Make, Model, and Year.
        return f"{self.make} {self.model} ({self.year})"

class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales')
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='sales')
    sale_date = models.DateField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        # We’ll see something like: “Sale of Toyota Corolla (2022) to Jack Smith on 2025-05-01”
        return f"Sale of {self.car} to {self.customer} on {self.sale_date}"
