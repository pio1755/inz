import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import SET_NULL

from django.utils.translation import ugettext_lazy as _

# Create your models here.
from accounts.models import CustomUser


class Class(models.Model):
    class_name = models.CharField(
        verbose_name=_('Klasa'),
        max_length=255,
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):  # noqa: D105
        return f'{self.class_name}'

    class Meta:  # noqa: D106
        verbose_name = _('Klasa')


class Rooms(models.Model):
    room_name = models.CharField(
        _('Sala'),
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):  # noqa: D105
        return f'{self.room_name}'


class Lessons(models.Model):
    lesson_name = models.CharField(
        _('Lekcja'),
        max_length=200,
        blank=True,
        null=True,
    )
    Klasa = models.ForeignKey(
        Class,
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name='Classes',
    )
    Sala = models.ForeignKey(
        Rooms,
        blank=True,
        null=True,
        on_delete=SET_NULL,
        related_name='Rooms',
    )
    Date_start = models.DateTimeField(
        _('Date start'),
        blank=True,
        null=False,
        default=datetime.datetime.now()
    )
    Date_stop = models.DateTimeField(
        _('Date stop'),
        blank=True,
        null=False,
        default=datetime.datetime.now()
    )
    Nauczyciel = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='teacher',
        limit_choices_to={'is_teacher': True},
    )

    def changeYear(self):
        return datetime.datetime.strptime(str(self.Date_start),"%Y-%m-%d %H:%M:%S%z").strftime("%Y/%m/%d %H:%M:%S%z")
    def changeYearOver(self):
        return datetime.datetime.strptime(str(self.Date_stop),"%Y-%m-%d %H:%M:%S%z").strftime("%Y/%m/%d %H:%M:%S%z")


class UserInClass(models.Model):
    Uczen = models.OneToOneField(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='student',
        limit_choices_to={'is_student': True},
    )
    Klasa = models.ForeignKey(
        Class,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='classes',
    )


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
