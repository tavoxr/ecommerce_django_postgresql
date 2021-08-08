from django.shortcuts import render, redirect
from ..models import *


def dashboard(request):

    context = {}
    return render(request, 'ecommerce/pages/Dashboard.html', context)