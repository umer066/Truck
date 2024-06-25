from django.db import models

class DriverProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=50)
    medical_history = models.TextField(blank=True)
    fitness_records = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
