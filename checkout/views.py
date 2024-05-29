from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe 

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))
    
            
    cart_in_process = bag_contents(request)
    total = cart_in_process['grand_total']
    stripe_total = round(total * 100)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PLieKL08Ezuq05rxo1nXl2Ne1jOMmMDl1qjjvXHr4AiyrBmU0o3ibyY3jENm7cHvQVpBbtGDkb7y5wsKmiVKv7b00czStMIDG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
