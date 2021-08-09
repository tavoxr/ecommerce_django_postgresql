from django.shortcuts import render, redirect
from ..models import *
from ..decorators import admin_only
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
@admin_only
def dashboard(request):
    
    

    context = {}
    return render(request, 'ecommerce/pages/Dashboard.html', context)