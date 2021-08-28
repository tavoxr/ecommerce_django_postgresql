from ecommerce.viewsets.orders import orders
from ecommerce.viewsets.cart import cart
from ecommerce.viewsets.checkout import checkout
from ecommerce.viewsets.login import loginPage
from django.urls import path
from .viewsets import *

urlpatterns = [
    path('', store, name='store' ),
    path('register/', registerUser, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name= 'logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('orders/', orders, name='orders'),
    path('orderItems/<int:id>/', orderItems, name='orderItems'),
    path('product/<int:id>/', viewProduct, name= "product"),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_cart, name='update_item' ),
    path('process_order/', processOrder, name='process_order')
]