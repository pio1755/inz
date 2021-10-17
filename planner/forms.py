from django import forms
from django.forms import ModelForm

from .models import CustomSettings

class CustomSettingsForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = CustomSettings

        fields = '__all__'

