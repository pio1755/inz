from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from accounts.models import CustomUser
from .models import CustomSettings, Class, Rooms


class CustomSettingsForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = CustomSettings

        fields = '__all__'

class CustomUserForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = CustomUser

        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'Class',
        ]

class ClassPanelForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Class

        fields = '__all__'

class RoomsPanelForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Rooms

        fields = '__all__'