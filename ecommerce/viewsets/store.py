from django.shortcuts import render, redirect



def store(request):

    print('request.user', request)
    context = {}
    return render(request, 'ecommerce/pages/Store.html', context)