from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Class(models.Model):
    class_name = models.CharField(
        _('Class name'),
        max_length=255,
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):  # noqa: D105
        return f'{self.class_name}'


class Rooms(models.Model):
    room_name = models.CharField(
        _('Room Name'),
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):  # noqa: D105
        return f'{self.room_name}'


class CustomSettings(models.Model):  # noqa: D101

    LANG = [
        ['pl', 'Polish'],
        ['en-us', 'English'],
    ]
    language = models.CharField(
        _('Language'),
        choices=LANG,
        default=1,
        max_length=5,
    )
