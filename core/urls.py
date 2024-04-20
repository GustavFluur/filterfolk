from django.urls import path
from core.views import index,contact, home


app_name = "core"


urlpatterns = [
    path('home/', views.home), 
    path('', views.index),
    path('contact/', views.contact),
    
]