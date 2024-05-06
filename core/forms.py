from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
    
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
    
    }))
    



class ProfileRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ('firstname','lastname','username', 'email', 'password1', 'password2')

    firstname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter First Name',
    
    }))

    lastname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Last Name',
    
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email Address',
    
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
    
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Choose Password',
    
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Repeat Password',
    
    }))