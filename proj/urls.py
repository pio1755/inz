"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views


from planner.views import CustomSettingsUpdateView, register_request, CustomUserUpdateView, ClassView, ClassUpdateView, \
    class_delete, RoomView, RoomUpdateView, room_delete, LessonView, LessonUpdateView, lesson_delete, UICView, \
    UICUpdateView, uic_delete
from proj import settings

urlpatterns = [
                  path('admin/', admin.site.urls, name='panel_admin'),
                  path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
                  path('', TemplateView.as_view(template_name='main_page.html'), name='main_page'),
                  path('admin/rosetta/', include('rosetta.urls')),
                  path('plan/', CustomSettingsUpdateView.as_view(), name='plan'),
                  path('settings/', CustomSettingsUpdateView.as_view(), name='settings'),
                  path('settings/user_profile', CustomUserUpdateView.as_view(), name='user_profile'),
                  path('settings/class_panel', ClassView.as_view(), name='class_panel'),
                  path('settings/updateclass_panel/<int:pk>/', ClassUpdateView.as_view(), name='updateclass_panel'),
                  path('remove_class/<int:pk>/', class_delete, name='class_delete'),
                  path('settings/room_panel', RoomView.as_view(), name='room_panel'),
                  path('settings/updateroom_panel/<int:pk>', RoomUpdateView.as_view(), name='updateroom_panel'),
                  path('remove_room/<int:pk>/', room_delete, name='room_delete'),

                  path('settings/lesson_panel', LessonView.as_view(), name='lesson_panel'),
                  path('settings/updatelesson_panel/<int:pk>', LessonUpdateView.as_view(), name='updatelesson_panel'),
                  path('remove_lesson/<int:pk>/', lesson_delete, name='lesson_delete'),

                  path('settings/uic_panel', UICView.as_view(), name='uic_panel'),
                  path('settings/updateuic_panel/<int:pk>', UICUpdateView.as_view(), name='updateuic_panel'),
                  path('remove_uic/<int:pk>/', uic_delete, name='uic_delete'),

                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                  path("register/", register_request, name='register')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
