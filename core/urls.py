from django.contrib.auth import views as auth_views
from django.urls import path
from .views import contact, register

from .forms import SignInForm


app_name = "core"


urlpatterns = [
    
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('signIn/', auth_views.LoginView.as_view(template_name='core/signIn.html', authentication_form=SignInForm), name='signIn'),
    
]