from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def loginPage(request):

    context = {}

    if request.method == 'POST':
        username =  request.POST.get('username')
        password =  request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('store')
        
        else:
            messages.info(request, 'Username or Password are incorrect')
            

    return render(request, 'ecommerce/pages/Login.html', context )



def logoutUser(request):
    logout(request)

    return redirect('login')
