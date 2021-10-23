from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.forms import CheckboxSelectMultiple

from .models import CustomSettings

admin.site.register(CustomSettings)