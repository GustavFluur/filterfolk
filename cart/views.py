from django.shortcuts import render
from django.contrib import messages


def view_cart(request):
    """ A view to render the bag contents page """

    return render(request, 'cart/cart.html')

