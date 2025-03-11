from django.contrib import admin
from .models import Shoe

@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock')  # Display these fields in the admin panel
    search_fields = ('name', 'brand')  # Add search functionality
    list_filter = ('brand', 'price')  # Add filtering options
