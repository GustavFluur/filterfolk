from django.shortcuts import render
from product.models import Category, Product

# Create your views here.
def index(request):
    products = Product.objects.filter()[:4]
    for product in products:
        product.price = round(product.price)
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'categories': categories,
        'products': products, 

    })

def home(request):
    return render(request, 'core/home.html')


def contact(request):
    return render(request,'core/contact.html')
 