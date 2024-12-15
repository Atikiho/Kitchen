from django import forms

from Kitchen_app.models import Dish, DishType
from Accounts.models import Cook


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=Cook.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    price = forms.DecimalField(min_value=1)

    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class DishFormSearch(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    min_price = forms.DecimalField(
        min_value=1,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Min price"}),
    )
    max_price = forms.DecimalField(
        min_value=1,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Max price"}),
    )
    dish_type = forms.ModelMultipleChoiceField(
        queryset=DishType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
