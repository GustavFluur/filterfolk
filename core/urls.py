from django.contrib.auth import views as auth_views
from django.urls import path
from .views import contact, home, register

from .forms import SignInForm


app_name = "core"


urlpatterns = [
    path('', home, name='home'), 
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('signIn/', auth_views.LoginView.as_view(template_name='core/signIn.html', authentication_form=SignInForm), name='signIn'),
    
]