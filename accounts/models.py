"""Account models."""
# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# 3rd-party
from colorfield.fields import ColorField


class CustomUser(AbstractUser):  # noqa: D101
    CLASS = [
        ['--', '--'],
        ['1A', '1A'],
        ['1B', '1B'],
        ['1C', '1C'],
        ['2A', '2A'],
        ['2B', '2B'],
        ['3C', '2C'],
    ]

    LANG = [
        ['pl', 'Polish'],
        ['en-us', 'English'],

    ]
    is_planner = models.BooleanField(default=False, verbose_name=_('Is planner'))
    is_teacher = models.BooleanField(default=False, verbose_name=_('Is teacher'))

    Class = models.CharField(
        _('Class'),
        choices=CLASS,
        default=1,
        max_length=2,
    )
    language = models.CharField(
        _('Language'),
        choices=LANG,
        default=1,
        max_length=5,
    )
