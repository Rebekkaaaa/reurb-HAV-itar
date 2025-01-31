from django.db import models
from django.contrib.auth.models import User


class Marker(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='markers/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
