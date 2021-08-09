from django.shortcuts import render, redirect
from ..models import *
from django.contrib.auth.models import Group, User
from ..decorators import admin_only
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@admin_only
def dashboard(request):
    group = Group.objects.get(name = 'customer')
    user = request.user
    customers = User.objects.filter(groups = group )
    orders =  Order.objects.filter(user = user )
    

    context = {
        'customers': customers,
        'orders': orders,
    }
    return render(request, 'ecommerce/pages/Dashboard.html', context)