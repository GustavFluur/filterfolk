from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):

    return render(request, 'cart/cart.html')

def add_cart(request, item_id):
    pass

def update_cart(request, item_id):

    pass


def delete_cart(request, item_id):

    pass

