from django.shortcuts import render
from ..models import *
from ..utils import cartData
from django.contrib.auth.decorators import login_required
from ..forms import EditProfilePhotoForm
from django.core.files.storage import FileSystemStorage

@login_required(login_url='login')
def profile(request):

    profile = request.user.profile
    user = request.user

    print('use.phone', user)

    photoProfileForm = EditProfilePhotoForm()
    profileNew =  Profile.objects.get(id =  profile.id)

    if request.method == "POST":

        print("req.POST", request.POST)
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname =  request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        photo = request.POST.get('photo')

        print('username', username)

        user.username =  username
        user.first_name = firstname
        user.last_name = lastname
        user.email =  email
        user.save()

        profile.phone =   phone
        profile.save()

        

       # photoProfileForm = EditProfilePhotoForm(request.POST, request.FILES,   instance= profileNew )
        
        #if photoProfileForm.is_valid():
        #   photoProfileForm.save()

        


        


        

    context  ={
        'user': user,
        'profile': profile,
        'photoProfileForm': photoProfileForm
       
    }
   # return render(request,'ecommerce/pages/Profile.html', context)
    return render(request,'ecommerce/pages/Profile.html', context)

