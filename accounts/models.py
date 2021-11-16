"""Account models."""
# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import SET_NULL
from django.utils.translation import ugettext_lazy as _

# 3rd-party
from colorfield.fields import ColorField

# from planner.models import Class


class CustomUser(AbstractUser):  # noqa: D101

    is_planner = models.BooleanField(default=False, verbose_name=_('Is planner'))
    is_teacher = models.BooleanField(default=False, verbose_name=_('Is teacher'))

    def __str__(self):  # noqa: D105
        return f'{self.get_full_name()}'
