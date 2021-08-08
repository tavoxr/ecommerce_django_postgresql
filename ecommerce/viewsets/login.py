from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..decorators import unauthenticated_user

@unauthenticated_user
def loginPage(request):

    context = {}

    if request.method == 'POST':
        username =  request.POST.get('username')
        password =  request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            if request.user.groups.all()[0].name == 'admin':
                return redirect('dashboard')
            else:
                return redirect('store')
        
        else:
            messages.info(request, 'Username or Password are incorrect')
            

    return render(request, 'ecommerce/pages/Login.html', context )



def logoutUser(request):
    logout(request)

    return redirect('login')
