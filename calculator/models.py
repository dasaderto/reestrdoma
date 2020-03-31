# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

from core.models import TimeStampedModel, User


class CalculatorProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = CalculatorProfile(user=instance)
        profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.calculator_profile.save()


