from django.db import models

class Truck(models.Model):
    license_plate = models.CharField(max_length=15, unique=True)
    model = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    capacity = models.FloatField(help_text="Capacity in tons")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.license_plate
