from django.urls import path
from .views import product_list, add_shoe, cart_detail, add_to_cart, remove_from_cart, checkout, my_orders, about_us, faq


urlpatterns = [
    path('', product_list, name="product_list"),
    path('add/', add_shoe, name="add_shoe"),  # New URL for adding shoes
]

#To be reformated
urlpatterns += [
    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<int:shoe_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:shoe_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('my-orders/', my_orders, name='my_orders'),
    path('about/', about_us, name='about'),
    path('faq/', faq, name='faq'),
]
