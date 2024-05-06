from django.shortcuts import render, redirect
from product.models import Category, Product
from django.contrib import messages

from .forms import ProfileRegister

# Create your views here.
def products_list(request):
    products = Product.objects.filter()
    for product in products:
        product.price = round(product.price)
    categories = Category.objects.all()
    
    return render(request, 'core/products.html', {
        'categories': categories,
        'products': products, 

    })

def home(request):
    return render(request, 'core/home.html')


def contact(request):
    return render(request,'core/contact.html')


def register(request):

    if request.method == 'POST':
        form = ProfileRegister(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/signIn/')
    else:        
        form = ProfileRegister()


    return render(request, 'core/register.html', {
        'form': form
    })
 