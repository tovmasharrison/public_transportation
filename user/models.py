from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User 
from django.db.models.signals import post_save

from helpers.image_paths import upload_profile_image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_profile_image, blank=True) # Default profile image petq a drvi

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def send_profile_signal(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()