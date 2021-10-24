from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from accounts.forms import NewUserForm
from .forms import CustomSettingsForm, CustomUserForm
from .models import CustomSettings
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.contrib import messages
from accounts.models import CustomUser


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
    template_name = 'user_profile.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('user_profile')
    pk = None

    def get_object(self, queryset=None):  # noqa: D102
        return get_user_model().objects.get(pk=self.pk)

    def dispatch(self, request, *args, **kwargs):  # noqa: D102
        self.pk = request.user.pk
        return super().dispatch(request, *args, **kwargs)
