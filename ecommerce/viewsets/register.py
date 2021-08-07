import django
from django.shortcuts import render, redirect
from ..forms import RegisterUserForm
from ..models import *
from django.contrib import messages
import re 


def registerUser(request):

    form =  RegisterUserForm()
    
    context = {
        'form': form
    }

    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        passValidated = re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}', pass1)

        if passValidated:
            
            if pass1 == pass2:
                form = RegisterUserForm(request.POST)

                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')

                    messages.success(request, 'Account was created for' + username )
                    return redirect('login')
            else:
                messages.error(request, "Passwords don't match")
        else:
            messages.error(request, 'Password not valid')


    return render(request, 'ecommerce/pages/Register.html', context )