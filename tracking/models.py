from django.db import models
from booking.models import Booking

class Tracking(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tracking for Booking {self.booking.id}"
