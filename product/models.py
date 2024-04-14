from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self):
        return self.name