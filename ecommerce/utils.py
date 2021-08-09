import json
from .models import *


def cookieCart(request):

    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    
    print('cart from cookieCart', cart)
    items = []
    order = {'get_total_order_ammount': 0, 'get_total_items':0}
    cartItems = order['get_total_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id = i)
            total = (product.price * cart[i]['quantity'])

            order['get_total_order_ammount'] += total
            order['get_total_items'] += cart[i]['quantity']

            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'image': product.image,
                    'category': product.category,
                    'brand': product.brand,
                    'description': product.description,
                },
                'quantity': cart[i]['quantity'],
                'get_total_ammount': total,
            }    
            
            items.append(item)
        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items }



def cartData(request):

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user = user, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_items
    else:
        cookieData =  cookieCart(request)
        cartItems = cookieData['cartItems']
        order =  cookieData['order']
        items =  cookieData['items']

    
    return {'order': order, 'items': items, 'cartItems': cartItems}





def guestOrder(request, data):
    print('User is not logged in...')  
    print('COOKIES', request.COOKIES)
        
    name = data['form']['name']
    email =  data['form']['email']

    cookieData =  cookieCart(request)
    items = cookieData['items']

    user, created = User.objects.get_or_create( 
        email = email
        )
    
    user.username = name
    user.save()
    
    order =  Order.objects.create(
        user =  user,
        complete = False
    )

    for item in items:
        product = Product.objects.get(id= item['product']['id'])

        orderItem = OrderItem.objects.create(
            product = product,
            order = order,
            quantity = item['quantity']
        )


    return user, order