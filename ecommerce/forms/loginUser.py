from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from ..models import Profile


class UserLoginForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1']
