from django import forms

from .models import Product

STYLE_CLASSES = 'col-md-6 offset-md-6'

class AddNewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': STYLE_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': STYLE_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': STYLE_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': STYLE_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': STYLE_CLASSES
            }),
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image',)
        widget = {

            'name': forms.TextInput(attrs={
                'class': STYLE_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': STYLE_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': STYLE_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': STYLE_CLASSES
            }),
        }