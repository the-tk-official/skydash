from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from users.models import Profile


def createUser(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwards):
    user = instance.user
    user.delete()


post_save.connect(createUser, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
