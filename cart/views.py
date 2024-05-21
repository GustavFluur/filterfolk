from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from product.models import Product
from django.http import JsonResponse
from django.contrib import messages



def cart_total(request):

    return render(request, 'cart/cart.html', {})



def add_cart(request, product_id):
    cart = Cart(request)
	# test for POST
	
    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, ("Product Added To Shopping Cart..."))
    
    return response


def update_cart(request, item_id):

    pass


def delete_cart(request, item_id):

    pass

