# """Admin View."""
# # Django
# from django import forms
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm
# from django.utils.translation import gettext_lazy as _
#
# # Local
# from .models import CustomUser
#

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'is_planner', 'is_teacher',
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_planner', 'is_teacher', 'is_superuser', 'Class', 'language'
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_planner', 'is_teacher')
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)

#
# class UserCreationFormExtended(UserCreationForm):   # noqa: D101
#     def __init__(self, *args, **kwargs):   # noqa: D107
#         super(UserCreationFormExtended, self).__init__(*args, **kwargs)
#         self.fields['email'] = forms.EmailField(label=_('E-mail'), max_length=75)
#
#
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):  # noqa: D101
#     add_form = UserCreationFormExtended
#     list_display = [
#         'username',
#         'first_name',
#         'last_name',
#         'is_active',
#     ]
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'birthday_date')}),
#         (_('Permissions'), {
#             'fields': (
#                 'is_active',
#                 'is_staff',
#                 'is_planner',
#                 'is_superuser',
#                 'is_banned',
#                 'groups',
#                 'user_permissions',
#             ),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2'),
#         }),
#     )
