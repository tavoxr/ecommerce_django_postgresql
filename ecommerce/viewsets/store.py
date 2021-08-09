from django.shortcuts import render, redirect
from ..models import Product, Order
from ..utils import cartData

def store(request):

    data = cartData(request)
    cartItems = data['cartItems']
    
    products = Product.objects.all()

    context = {
        'products': products,
        'cartItems': cartItems
    }
    return render(request, 'ecommerce/pages/Store.html', context)