from django.contrib import admin

# Register your models here.
from django.forms import CheckboxSelectMultiple

from .models import CustomSettings

admin.site.register(CustomSettings)