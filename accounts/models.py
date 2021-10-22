from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ListUserModel(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
