from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.search_products, name='search'),
    path('products/', views.products_list, name='inventory'),
    path('newproduct/', views.add_new_product, name='add_new_product' ),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/delete/', views.delete_product, name='delete'),
    path('<int:pk>/edit/', views.edit_product, name='edit'),

]