from django.urls import path
from .views import products_list,contact, home, register


app_name = "core"


urlpatterns = [
    path('', home, name='home'), 
    path('products/', products_list),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    
]