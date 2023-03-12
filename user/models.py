from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from helpers.image_paths import default_profile_image, upload_profile_image


User = get_user_model()


class Profile(models.Model):
    """ User Profile model """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_profile_image, default=default_profile_image)

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def send_profile_signal(sender, created, instance, **kwargs):
    """ Automatically creates a profile when user is registered """

    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
