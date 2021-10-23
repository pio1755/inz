from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import CustomSettingsForm
from .models import CustomSettings
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
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
