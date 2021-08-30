from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from ..models import Profile



class EditProfilePhotoForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'avatar',
        ]
