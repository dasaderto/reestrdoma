from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from rest_framework_simplejwt.tokens import RefreshToken


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta(object):
        abstract = True


class User(AbstractUser):
    phone = models.CharField(max_length=30, blank=True)
    bitrix_id = models.IntegerField(null=True)


def get_tokens_for_user(user: User):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }