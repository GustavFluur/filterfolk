from django.urls import path
from core.views import index,contact


app_name = "core"


urlpatterns = [ 
    path('', views.index),
    path('contact/', views.contact)
]