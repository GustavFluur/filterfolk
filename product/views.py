from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    #related_merchandises = product.objects.filter(category=merchandise.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'product/product_detail.html', {
        'product': product,
        #'related_merchandises': related_merchandises
    })