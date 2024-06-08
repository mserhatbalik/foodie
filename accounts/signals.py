"""
This module defines a signal receiver function for the User model.

The post_save_create_profile_receiver function is connected to the post_save signal of the User model. This function is called every time an instance of User is saved. If a new User instance is created, it creates a corresponding UserProfile instance. If an existing User instance is saved, it tries to update the corresponding UserProfile instance. If the UserProfile instance does not exist, it creates a new one.

Imported Modules:
    - django.db.models.signals: Used to import the post_save signal.
    - django.dispatch: Used to import the receiver decorator.
    - accounts.models: Used to import the UserProfile and User models.

Functions:
    - post_save_create_profile_receiver: A signal receiver function for the User model.
"""
# Import necessary modules and classes
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserProfile, User

# This signal is used to create a profile for a user when a user is created
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        # If the profile does not exist, create a new profile
        UserProfile.objects.create(user=instance)
    else:
        try:
            # If the profile exists, update the profile
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # If the profile does not exist, create a new profile
            UserProfile.objects.create(user=instance)