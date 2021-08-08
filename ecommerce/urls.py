from ecommerce.viewsets.login import loginPage
from django.urls import path
from .viewsets import *

urlpatterns = [
    path('', store, name='store' ),
    path('register/', registerUser, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name= 'logout'),
    path('dashboard/', dashboard, name='dashboard'),

]