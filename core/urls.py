from django.urls import path
from .views import products_list,contact, home


app_name = "core"


urlpatterns = [
    path('home/', home, name='home'), 
    path('products/', products_list),
    path('contact/', contact, name='contact'),
    
]