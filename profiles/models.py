from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio updated")
    avatar = models.ImageField(upload_to='avatars', default='no_picture.jpeg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"profile of {self.user.username}"


@receiver(post_save, sender=User)


def post_create_profile(sender, instance, created, **kwargs):


    if created:
        Profile.objects.create(user=instance)
