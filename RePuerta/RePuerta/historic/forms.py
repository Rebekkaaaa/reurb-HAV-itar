from django import forms
from . import models


class AddMarker(forms.ModelForm):
    class Meta:
        model = models.Marker
        fields = ['name', 'image', 'latitude', 'longitude', 'description']
