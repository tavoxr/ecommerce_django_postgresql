from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User
from ..models import Profile
from django.dispatch import receiver


@receiver(post_save,sender= User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        users = User.objects.all().count()
        print('users', users)
        admin = 'admin'
        customer = 'customer'

        if int(users) <= 2:
            group, created = Group.objects.get_or_create(name = admin)
            instance.is_staff  = True
            instance.is_superuser = True
            instance.save()
        else:
            group, created = Group.objects.get_or_create(name = customer)


        instance.groups.add(group) #instance is user was created

        Profile.objects.create(
            user = instance
        )

        print('Profile created')
