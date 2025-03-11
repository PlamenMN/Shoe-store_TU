from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Shoe
from .forms import ShoeForm

@login_required
def add_shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to shoe list page
    else:
        form = ShoeForm()
    
    return render(request, 'products/add_shoe.html', {'form': form})

@login_required
def product_list(request):
    shoes = Shoe.objects.all()
    return render(request, "products/product_list.html", {"shoes": shoes})
