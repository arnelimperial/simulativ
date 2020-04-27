from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Profile
from django.dispatch import receiver

User = getattr(settings, 'AUTH_USER_MODEL')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
    # user = instance
    # if created:
    #     profile = Profile(user=user)
    #     profile.save()

#post_save.connect(create_profile, sender=User)
