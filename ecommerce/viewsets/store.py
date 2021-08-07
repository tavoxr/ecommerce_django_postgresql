from django.shortcuts import render, redirect



def store(request):

    context = {}
    return render(request, 'ecommerce/pages/Store.html', context)