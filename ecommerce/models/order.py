from django.contrib.auth.models import User
from django.db import models
from .profile import Profile
from .products import Product



class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete= models.SET_NULL)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['-date_created',]

    def __str__(self):
        return f'Order {self.id}: {self.user.username} - complete:{self.complete}'


    @property
    def get_total_order_ammount(self):
        orderItems = self.orderitem_set.all()
        total = 0

        for orderItem in orderItems:
             total += orderItem.get_total_ammount
        
        return total

    
    @property
    def get_total_items(self):
        orderItems =  self.orderitem_set.all()
        total = 0

        for orderItem in orderItems:
            total +=  orderItem.quantity

        return total

   




class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    quantity =  models.IntegerField(default=0, null=True, blank=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.product} - order:{self.order.id} '


    @property
    def get_total_ammount(self):
 
        total = self.product.price * self.quantity

        return total