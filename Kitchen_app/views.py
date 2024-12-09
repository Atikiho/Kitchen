from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from Kitchen_app.forms import (
    CookForm,
    DishForm,
    DishTypeForm,
    DishFormSearch,
    CookUpdateForm
)
from Kitchen_app.models import Cook, Dish, DishType


class Index(generic.ListView):
    model = Cook
    template_name = "Kitchen/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["Cooks"] = Cook.objects.all()
        context["Dishes"] = Dish.objects.all()
        context["DishTypes"] = Dish.objects.all()
        return context


class CookList(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "Kitchen/cook-list.html"
    paginate_by = 5


class CookDetail(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "Kitchen/cook-detail.html"


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


class DishList(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "Kitchen/dish-list.html"
    paginate_by = 5
    queryset = Dish.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishList, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        min_price = self.request.GET.get("min_price", "")
        max_price = self.request.GET.get("max_price", "")
        dish_type = self.request.GET.getlist("dish_type", "")

        context["search_form"] = DishFormSearch(
            initial={
                "name": name,
                "min_price": min_price,
                "max_price": max_price,
                "dish_type": dish_type,
            }
        )
        return context

    def get_queryset(self):
        form = DishFormSearch(self.request.GET)

        if form.is_valid():
            name = form.cleaned_data["name"]
            min_price = form.cleaned_data["min_price"]
            max_price = form.cleaned_data["max_price"]
            dish_type = form.cleaned_data["dish_type"]

            queryset = self.queryset

            if name:
                queryset = queryset.filter(name__icontains=name)
            if min_price is not None:
                queryset = queryset.filter(price__gte=min_price)
            if max_price is not None:
                queryset = queryset.filter(price__lte=max_price)
            if dish_type:
                queryset = queryset.filter(dish_type__in=dish_type)

            return queryset

        return self.queryset


class DishDetail(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "Kitchen/dish-detail.html"


class DishCreate(LoginRequiredMixin, generic.CreateView):
    model = Dish
    template_name = "Kitchen/form.html"
    form_class = DishForm
    success_url = reverse_lazy("dish-list")


class DishDelete(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "Kitchen/delete-confirm.html"
    success_url = reverse_lazy("dish-list")


class DishUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "Kitchen/form.html"
    success_url = reverse_lazy("dish-list")


class DishTypeList(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "Kitchen/dish-type-list.html"
    paginate_by = 5


class DishTypeCreate(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "Kitchen/form.html"
    success_url = reverse_lazy("dish-type-list")


class DishTypeDelete(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "Kitchen/delete-confirm.html"
    success_url = reverse_lazy("dish-type-list")


class DishTypeUpdate(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "Kitchen/form.html"
    success_url = reverse_lazy("dish-type-list")
