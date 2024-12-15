from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from Kitchen_app.forms import (
    DishForm,
    DishTypeForm,
    DishFormSearch,
)
from Kitchen_app.models import Dish, DishType
from Accounts.models import Cook


class Index(generic.ListView):
    model = Cook
    template_name = "Kitchen/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["Cooks"] = Cook.objects.all()
        context["Dishes"] = Dish.objects.all()
        context["DishTypes"] = DishType.objects.all()
        return context


class DishList(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "Kitchen/dish-list.html"
    paginate_by = 5

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

            queryset = Dish.objects.select_related("dish_type")

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
    queryset = Dish.objects.prefetch_related()


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
