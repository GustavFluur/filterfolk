from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category
from .forms import AddNewProductForm, EditProductForm


def products_list(request):
    products = Product.objects.filter()
    for product in products:
        product.price = round(product.price)
    categories = Category.objects.all()
    
    return render(request, 'product/inventory.html', {
        'categories': categories,
        'products': products, 

    })

def search_products(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    products = Product.objects.filter()

    if category_id:
        products = products.filter(category_id=category_id)

    if query:
         products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/products.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),   
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[0:3]

    return render(request, 'product/product_detail.html', {
        'product': product,
        'related_products': related_products
    })



@login_required 
def add_new_product(request):
        if request.method == 'POST':
            form = AddNewProductForm(request.POST, request.FILES)
            
            if form.is_valid():
                product = form.save(commit=False) #for creating a new product without saving into DB
                product.save()

                return redirect('product:product_detail', pk=product.id)
        else:
            form = AddNewProductForm()

        return render(request, 'product/product_form.html',{
            'form': form,
            'title': 'Add New Product',

        })


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()

    return redirect(reverse('products')) # Use reverse to get back to the products page


@login_required 
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            return redirect('product:product_detail', pk=product.id)
    else:        
        form = EditProductForm(instance=product)

    return render(request, 'product/product_form.html', {
        'form': form,
        'title': 'Edit Product',

    })