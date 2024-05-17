from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

