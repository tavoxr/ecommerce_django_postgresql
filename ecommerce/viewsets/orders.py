from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import *
from ..utils import cartData

@login_required(login_url='login')
def orders(request):

    data = cartData(request)
    cartItems = data['cartItems']

    user = request.user
    orders = Order.objects.filter(user = user, complete = True )

    print('user', user)
    print('orders', orders)

    context = {
        'orders': orders,
        'cartItems': cartItems
    }
    return render(request, 'ecommerce/pages/Orders.html', context)


@login_required(login_url='login')
def orderItems(request, id):

    data = cartData(request)
    cartItems = data['cartItems']

    user = request.user
    order = Order.objects.get(id = id)
    orderItems  = order.orderitem_set.all()

    context = {
        'order': order,
        'orderItems': orderItems,
        'cartItems': cartItems
    }
    return render(request, 'ecommerce/pages/OrderItems.html', context)
