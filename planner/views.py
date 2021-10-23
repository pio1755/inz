from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.forms import NewUserForm
from .forms import CustomSettingsForm, CustomUserForm
from .models import CustomSettings
from django.shortcuts import render, redirect
from django.contrib.auth import login
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

class CustomUserUpdateView(UpdateView):  # noqa: D101

    model = CustomUser
    template_name = 'user_profile.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('user_profile')

    def get_object(self, queryset=None):  # noqa: D102

        return self.model.objects.first()
