from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Shoe, Cart, CartItem, Order, OrderItem
from .forms import ShoeForm, CheckoutForm

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
def add_to_cart(request, shoe_id):
    shoe = get_object_or_404(Shoe, id=shoe_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        size = request.POST.get('size')

        item = CartItem.objects.create(cart=cart, shoe=shoe, quantity=quantity, size=size)

    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'products/cart_detail.html', {
        'cart': cart,
        'items': cart.items.all(),
        'total': cart.total_price()
    })

@login_required
def remove_from_cart(request, shoe_id):
    cart = get_object_or_404(Cart, user=request.user)
    item = cart.items.filter(shoe_id=shoe_id).first()
    if item:
        item.delete()
    return redirect('cart_detail')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.all()

    if not items:
        return redirect('cart_detail')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.delivery_service = "DHL"
            order.save()

            for item in items:
                # Deduct stock
                shoe = item.shoe
                if shoe.stock >= item.quantity:
                    shoe.stock -= item.quantity
                    shoe.save()
                else:
                    # Optionally handle insufficient stock
                    return render(request, 'products/checkout.html', {
                        'form': form,
                        'items': items,
                        'total': cart.total_price(),
                        'error': f"Not enough stock for {shoe.name}."
                    })

                # Create the order item
                OrderItem.objects.create(
                    order=order,
                    shoe=shoe,
                    quantity=item.quantity,
                    price=shoe.price,
                    size=item.size
                )

            # Clear the cart
            cart.items.all().delete()

            return render(request, 'products/checkout_success.html', {'order': order})
    else:
        form = CheckoutForm()

    return render(request, 'products/checkout.html', {
        'form': form,
        'items': items,
        'total': cart.total_price(),
    })

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'products/my_orders.html', {'orders': orders})

def product_list(request):
    brand = request.GET.get('brand')
    search = request.GET.get('q')
    per_page = request.GET.get('per_page', 10)
    sort_by = request.GET.get('sort')

    shoes = Shoe.objects.all()

    if brand:
        shoes = shoes.filter(brand__iexact=brand)

    if search:
        shoes = shoes.filter(name__icontains=search)

    if sort_by == 'price_asc':
        shoes = shoes.order_by('price')
    elif sort_by == 'price_desc':
        shoes = shoes.order_by('-price')
    elif sort_by == 'name_asc':
        shoes = shoes.order_by('name')
    elif sort_by == 'name_desc':
        shoes = shoes.order_by('-name')

    paginator = Paginator(shoes, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    brands = Shoe.objects.values_list('brand', flat=True).distinct()

    return render(request, 'products/product_list.html', {
        'page_obj': page_obj,
        'brands': brands,
        'selected_brand': brand,
        'search_query': search,
        'per_page': per_page,
        'sort_by': sort_by,
    })

def about_us(request):
    return render(request, 'pages/about.html')

def faq(request):
    return render(request, 'pages/faq.html')

