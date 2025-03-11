from django.urls import path
from .views import product_list, add_shoe

urlpatterns = [
    path('', product_list, name="product_list"),
    path('add/', add_shoe, name="add_shoe"),  # New URL for adding shoes
]
