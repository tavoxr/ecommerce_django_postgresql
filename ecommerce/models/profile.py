from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField

class Profile(models.Model):
    user =  models.OneToOneField(User,null=True, blank= True, on_delete= models.CASCADE)
    avatar = models.ImageField(null=True, blank=True)
    phone =  models.CharField(max_length=50, null=True, blank=True)
    date_created =  models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username