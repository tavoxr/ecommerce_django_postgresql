from django.urls import path
from .viewsets import *

urlpatterns = [
    path('', store, name='store' ),
    path('register/', registerUser, name='register'),

]