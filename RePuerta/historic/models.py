from django.db import models
from django.contrib.auth.models import User

# Create your models here.s


# class Location(models.Model):
#     name = models.CharField(max_length=200)
#     latitude = models.FloatField()
#     longitude = models.FloatField()

#     def __str__(self):
#         return self.name

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
