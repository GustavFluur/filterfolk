from django.urls import path
from core.views import index


app_name = "core"


urlpatterns = [ 
    path("home", views.index)
]