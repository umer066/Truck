from django.db import models
from drivers.models import DriverProfile

class MonitorStatus(models.Model):
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver} - {self.status}"
