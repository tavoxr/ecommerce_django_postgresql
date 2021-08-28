import datetime
from django.shortcuts import render, redirect
from ..models import *
from django.contrib.auth.models import Group, User
from ..decorators import admin_only
from django.contrib.auth.decorators import login_required
from ..utils import cartData

@login_required(login_url='login')
#@admin_only
def dashboard(request):

    data = cartData(request)
    cartItems = data['cartItems']

    group = Group.objects.get(name = 'customer')
    user = request.user

    customers = User.objects.filter(groups = group )
    lastOrders =  Order.objects.filter(user = user, complete= True)[0:5]
    orders = Order.objects.filter(user = user, complete= True)
    currentMonth =  datetime.date.today().month
    
    
    print('currentMonth', currentMonth)
    
    totalAmmountSpent = 0
    totalAmmountSpentPerMonth = 0
    totalOrdersThisMonth = 0 

    for order in orders:
        totalAmmountSpent += order.get_total_order_ammount

        if currentMonth == order.date_created.month:
            totalAmmountSpentPerMonth += order.get_total_order_ammount
    
        if currentMonth == order.date_created.month:
            totalOrdersThisMonth += 1
    
    
    #  lastOrders = Order.objects.filter()
    #print('request', request.user.groups.all()[0])
    
    if user.groups.filter(name= "admin").exists():
    
        context = {
        'customers': customers,
        'lastOrders': lastOrders,
        'orders': orders,
        'cartItems': cartItems,
        'totalAmmountSpent': totalAmmountSpent,
        'totalAmmountSpentPerMonth': totalAmmountSpentPerMonth,
        'totalOrdersThisMonth' : totalOrdersThisMonth
        
        }
        return render(request, 'ecommerce/pages/Dashboard.html', context)
    else:
        context = {    
        'orders': orders,
        'lastOrders': lastOrders,
        'cartItems': cartItems,
        'totalAmmountSpent': totalAmmountSpent,
        'totalAmmountSpentPerMonth': totalAmmountSpentPerMonth,
        'totalOrdersThisMonth' : totalOrdersThisMonth




        }
        return render(request, 'ecommerce/pages/CustomerDashboard.html', context)
