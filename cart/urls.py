from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_total, name='cart_total'),
    path('add/<item_id>', views.add_cart, name='add_cart'),
    path('update/<item_id>', views.update_cart, name='update_cart'),
    path('delete/<item_id>', views.delete_cart, name='delete_cart'),

]