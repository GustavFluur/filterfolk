from django.urls import path
from core.views import products_list,contact, home


app_name = "core"


urlpatterns = [
    path('home/', views.home), 
    path('products/', views.products_list),
    path('contact/', views.contact),
    
]