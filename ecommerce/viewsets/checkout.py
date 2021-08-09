import json
from django.shortcuts import render, redirect
from ..models import *
from django.http import  JsonResponse
import datetime
from ..utils import cookieCart ,cartData, guestOrder



def checkout(request):

    data =  cartData(request)
    
    cartItems =  data['cartItems']
    order  = data['order']
    items = data['items']

    context={
        'order': order,
        'items': items,
        'cartItems': cartItems
    }

    return render(request, 'ecommerce/pages/Checkout.html', context)


def processOrder(request):
    print(f'data: {request.body}')
    data = json.loads(request.body)

    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        user =  request.user
        order, created = Order.objects.get_or_create(user = user, complete =False)
        
        shippingAddress =  ShippingAddress.objects.create(
            user = user,
            order =  order,
            address = data['shipping']['address'],
            city =  data['shipping']['city'],
            state =  data['shipping']['state'],
            zipcode =  data['shipping']['zipcode'],

        )

    else:
        user, order = guestOrder(request, data)



    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_total_order_ammount):
        order.complete = True
        
    order.save()


    return JsonResponse('Payment complete', safe=False)


