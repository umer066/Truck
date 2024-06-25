from django.db import models

class Compliance(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
