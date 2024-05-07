from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import AddNewProductForm


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[0:3]

    return render(request, 'product/product_detail.html', {
        'product': product,
        'related_products': related_products
    })



@login_required 
def add_new_product(request):
     form = AddNewProductForm()

     return render(request, 'product/product_form.html',{
        'form': form,
        'title': 'New Product',

     })