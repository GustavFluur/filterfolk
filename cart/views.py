from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from django.contrib import messages



def cart_total(request):

    return render(request, 'cart/cart.html', {})



def add_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):

    pass


def delete_cart(request, item_id):

    pass

