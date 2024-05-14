from django.shortcuts import render, redirect
from product.models import Category, Product
from django.contrib import messages

from .forms import ProfileRegister

# Create your views here.

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
 