from django import forms
from .models import Shoe
from .models import Order

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['name', 'brand', 'price', 'description', 'image', 'stock']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'payment_type']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'payment_type': forms.Select()
        }
