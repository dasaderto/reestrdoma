from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import User, TimeStampedModel


class Profile(models.Model):
    LEGAL = 'LEGAL_FACE'
    PHYSICAL = 'PHYSICAL_FACE'
    STATUSES = (
        (LEGAL, 'Юр. лицо'),
        (PHYSICAL, 'Физ. лицо'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUSES, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class House(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    flat_count = models.IntegerField(default=0)
    actual_date = models.DateTimeField(null=True)
    reestr_link = models.CharField(null=True, max_length=255)
    status = models.CharField(null=True, max_length=255)
    square = models.FloatField(null=True)
    rights = models.CharField(null=True, max_length=255)


class Order(TimeStampedModel):
    house = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cad_num = models.CharField(max_length=255)
    address = models.CharField(null=True, max_length=255)
    square = models.FloatField(null=True)
    type = models.CharField(null=True, max_length=255)
    xml_link = models.CharField(null=True, max_length=255)
    zip_link = models.CharField(null=True, max_length=255)
    html_link = models.CharField(null=True, max_length=255)
    xml_link_status = models.CharField(null=True, max_length=255)
    zip_link_status = models.CharField(null=True, max_length=255)
    html_link_status = models.CharField(null=True, max_length=255)
