from django.shortcuts import render, redirect
from ..models import *
from ..utils import cartData
from django.http import JsonResponse
import json

def cart(request):

    data = cartData(request)

    order = data['order']
    items = data['items']
    cartItems = data['cartItems']


    print('request.user', request.user)
    
    context = {
        'order': order,
        'items': items,
        'cartItems': cartItems

    }

    return render(request, 'ecommerce/pages/Cart.html', context)





def update_cart(request):
    
    data = json.loads(request.body)

    productId = data['productId']
    action = data['action']

    print('req.body', request.body)
    print(f'productId: {productId},  action: {action}')

    user = request.user
    product = Product.objects.get(id= productId)
    order, created = Order.objects.get_or_create(user = user, complete =False)

    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
        