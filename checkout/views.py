from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PLieKL08Ezuq05rxo1nXl2Ne1jOMmMDl1qjjvXHr4AiyrBmU0o3ibyY3jENm7cHvQVpBbtGDkb7y5wsKmiVKv7b00czStMIDG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
