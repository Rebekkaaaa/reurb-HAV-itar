from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Door(models.Model):
    title = models.CharField(max_length=75)
    image = models.ImageField(default='fallback.png', blank=True)
    height = models.CharField(max_length=3)
    width = models.CharField(max_length=3)
    pos_hinge_top = models.CharField(max_length=3)
    pos_hinge_middle = models.CharField(max_length=3)
    pos_hinge_bottom = models.CharField(max_length=3)
    pos_lock = models.CharField(max_length=3)
    MATERIAL = {
        "w": "wood",
        "m": "metal",
        "g": "glass",
        "o": "other"
    }
    material = models.CharField(max_length=3, choices=MATERIAL)
    WINGS = {
        "1": "1",
        "2": "2",
    }
    wings = models.CharField(max_length=1, choices=WINGS)
    MECHANISM = {
        "h": "hinged",
        "s": "sliding",
        "o": "other"
    }
    mechanism = models.CharField(max_length=1, choices=MECHANISM)
    FRAME = {
        "y": "yes",
        "n": "no",
    }
    frame = models.CharField(max_length=1, choices=FRAME, default="n")
    opening_height = models.CharField(max_length=3)
    opening_width = models.CharField(max_length=3)
    details = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    slug = models.SlugField(default='title')

    def __str__(self):
        return self.title
