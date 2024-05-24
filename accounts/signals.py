from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserProfile, User


# This signal is used to create a profile for a user when a user is created
@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        # If the profile does not exist, create a new profile
        UserProfile.objects.create(user=instance)
        print('Profile created!')
    else:
        try:
            # If the profile exists, update the profile
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # If the profile does not exist, create a new profile
            UserProfile.objects.create(user=instance)
            print('Profile does not exist! Created new one!')
        print('Profile updated!')
