from django.contrib import admin
from .models import Marker

# Register your models here.


@admin.register(Marker)
class MarkerAdmin(admin.ModelAdmin):
    # Customize columns displayed in the list view
    list_display = ('name', 'latitude', 'longitude')
    search_fields = ('name',)  # Add a search bar for ease of use
