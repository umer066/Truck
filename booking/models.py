from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TruckType(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()  # Specify capacity in tons or any other unit

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    confirmation = models.BooleanField(default=False)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.location.name} - {self.date}"
