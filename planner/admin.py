from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.forms import CheckboxSelectMultiple

from .models import CustomSettings, Class, Rooms

admin.site.register(CustomSettings)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = [
        'class_name',
    ]


@admin.register(Rooms)
class RoomsAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = [
        'room_name',
    ]
