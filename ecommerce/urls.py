from django.urls import path
from .viewsets import *

urlpatterns = [
    path('', store, name='store' ),

]