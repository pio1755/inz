from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from accounts.models import CustomUser
from .models import CustomSettings, Class, Rooms, UserInClass, Lessons


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
        ]


class ClassPanelForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Class

        fields = '__all__'


class RoomsPanelForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Rooms

        fields = '__all__'

class LessonPanelForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Lessons

        fields = '__all__'

        # def __init__(self, *args, **kwargs):  # noqa: D107
        #     super().__init__(*args, **kwargs)
        #     self.fields['teacher'].label_from_instance = lambda obj: f'{obj.get_full_name()}'


class UserInClassForm(ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = UserInClass
        #
        # def __init__(self, *args, **kwargs):  # noqa: D107
        #     super().__init__(*args, **kwargs)
        #     self.fields['User'].queryset = UserInClass.objects.filter(Class__isnull=True)

        fields = [
            'User',
            'Class',
        ]


