from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('newproduct/', views.add_new_product, name='add_new_product' ),
    path('<int:pk>/', views.product_detail, name='product_detail'),

]