from django.urls import path
from core.views import index,contact, home


app_name = "core"


urlpatterns = [ 
    path('', views.index),
    path('contact/', views.contact),
    path('home/', views.home),
]