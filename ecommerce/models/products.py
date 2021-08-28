from re import T
from django.db import models
from .category import Category

class Product(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.ImageField(default="productDefaultImg1.jpg",  null=True, blank= True)
    brand =  models.CharField( max_length=150, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f' {self.name} {self.price}'