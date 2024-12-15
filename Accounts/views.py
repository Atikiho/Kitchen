from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from Accounts.forms import CookForm, CookUpdateForm
from Accounts.models import Cook


class CookList(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "Kitchen/cook-list.html"
    paginate_by = 5


class CookDetail(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "Kitchen/cook-detail.html"
    queryset = Cook.objects.prefetch_related("dishes")


class CookCreate(generic.CreateView):
    model = Cook
    form_class = CookForm
    template_name = "registration/registration_form.html"
    success_url = reverse_lazy("index")


class CookDelete(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "Kitchen/delete-confirm.html"
    success_url = reverse_lazy("cook-list")


class CookUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    template_name = "registration/registration_form.html"
    form_class = CookUpdateForm
    success_url = reverse_lazy("cook-list")
