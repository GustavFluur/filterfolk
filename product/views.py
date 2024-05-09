from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, reverse, get_object_or_404, redirect
from .models import Product
from .forms import AddNewProductForm, EditProductForm


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