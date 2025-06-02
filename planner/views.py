from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView, TemplateView

from accounts.forms import NewUserForm
from .forms import CustomSettingsForm, CustomUserForm, ClassPanelForm, RoomsPanelForm, LessonPanelForm, UserInClassForm
from .models import CustomSettings, Class, Rooms, UserInClass, Lessons
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib import messages



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, "Registration successful.")
            return redirect(reverse_lazy("main_page"))
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


class CustomSettingsUpdateView(UpdateView):  # noqa: D101

    model = CustomSettings
    template_name = 'settings.html'
    form_class = CustomSettingsForm
    success_url = reverse_lazy('settings')

    def get_object(self, queryset=None):  # noqa: D102
        return self.model.objects.first()


@method_decorator(login_required(), name='dispatch')
class CustomUserUpdateView(UpdateView):  # noqa: D101

    model = get_user_model()
    template_name = 'settings/user_profile.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('user_profile')
    pk = None

    def get_object(self, queryset=None):  # noqa: D102
        return get_user_model().objects.get(pk=self.pk)

    def dispatch(self, request, *args, **kwargs):  # noqa: D102
        self.pk = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['settings'] = CustomSettings.objects.all()
        context['class'] = Class.objects.all()
        return context


class ClassView(CreateView):  # noqa: D101

    model = Class
    template_name = 'settings/plannerpanel/classpanel/classpanel.html'
    form_class = ClassPanelForm
    success_url = reverse_lazy('class_panel')

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['class_obj'] = Class.objects.all()
        return context


class ClassUpdateView(UpdateView):  # noqa: D101

    model = Class
    template_name = 'settings/plannerpanel/classpanel/editclass.html'
    form_class = ClassPanelForm
    success_url = reverse_lazy('class_panel')

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['class_obj'] = Class.objects.all()
        return context


def class_delete(request, pk):  # noqa: D103

    cl = get_object_or_404(Class, pk=pk)

    if request.method == 'POST':
        cl.delete()
        return redirect('/settings/class_panel')

    return render(request, 'settings/plannerpanel/classpanel/class_list.html', {'cl': cl})


class RoomView(CreateView):  # noqa: D101

    model = Rooms
    template_name = 'settings/plannerpanel/roomspanel/roomspanel.html'
    form_class = RoomsPanelForm
    success_url = reverse_lazy('room_panel')

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['room_obj'] = Rooms.objects.all()
        return context


class RoomUpdateView(UpdateView):  # noqa: D101

    model = Rooms
    template_name = 'settings/plannerpanel/roomspanel/editroom.html'
    form_class = RoomsPanelForm
    success_url = reverse_lazy('room_panel')

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['room_obj'] = Rooms.objects.all()
        return context


def room_delete(request, pk):  # noqa: D103

    cl = get_object_or_404(Rooms, pk=pk)

    if request.method == 'POST':
        cl.delete()
        return redirect('/settings/room_panel')

    return render(request, 'settings/plannerpanel/roomspanel/room_list.html', {'cl': cl})


class LessonView(CreateView):  # noqa: D101

    model = Lessons
    template_name = 'settings/plannerpanel/lessonspanel/lessonspanel.html'
    form_class = LessonPanelForm
    success_url = reverse_lazy('lesson_panel')

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['lesson_obj'] = Lessons.objects.all()
        context['class_obj'] = Class.objects.all()
        return context


class LessonUpdateView(UpdateView):  # noqa: D101

    model = Lessons
    template_name = 'settings/plannerpanel/lessonspanel/editlesson.html'
    form_class = LessonPanelForm
    success_url = reverse_lazy('lesson_panel')

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['lesson_obj'] = Lessons.objects.all()
        context['class_obj'] = Class.objects.all()
        return context


def lesson_delete(request, pk):  # noqa: D103

    cl = get_object_or_404(Lessons, pk=pk)

    if request.method == 'POST':
        cl.delete()
        return redirect('/settings/lesson_panel')

    return render(request, 'settings/plannerpanel/lessonspanel/lesson_list.html', {'cl': cl})


class UICView(CreateView):  # noqa: D101

    model = UserInClass
    template_name = 'settings/plannerpanel/UserInClass/uicpanel.html'
    form_class = UserInClassForm
    success_url = reverse_lazy('uic_panel')



    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['uic_obj'] = UserInClass.objects.all()
        context['class_obj'] = Class.objects.all()

        return context


class UICUpdateView(UpdateView):  # noqa: D101

    model = UserInClass
    template_name = 'settings/plannerpanel/UserInClass/edituic.html'
    form_class = UserInClassForm
    success_url = reverse_lazy('uic_panel')

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['uic_obj'] = UserInClass.objects.all()
        context['class_obj'] = Class.objects.all()
        return context


def uic_delete(request, pk):  # noqa: D103

    cl = get_object_or_404(UserInClass, pk=pk)

    if request.method == 'POST':
        cl.delete()
        return redirect('/settings/uic_panel')

    return render(request, 'settings/plannerpanel/UserInClass/uic_list.html', {'cl': cl})


class AllSchedulersView(TemplateView):  # noqa: D101
    template_name = 'plan.html'
    model = Lessons
    success_url = reverse_lazy('plan')

    def get_context_data(self, **kwargs):  # noqa: D102

        context = super().get_context_data(**kwargs)
        context['lessons'] = Lessons.objects.all()
        return context
