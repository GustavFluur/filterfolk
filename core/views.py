from django.shortcuts import render
from product.models import Category, Product

# Create your views here.
def index(request):
    products = Product.objects.filter()[:3]
    for product in products:
        product.price = round(product.price)
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'products': products, 

    }) 