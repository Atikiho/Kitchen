from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from Kitchen_app.models import Cook, Dish, DishType


class CookForm(UserCreationForm):
    years_of_experience = forms.IntegerField(
        min_value=0,
        max_value=80,
        label="Years of experience"
    )
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience", "email")


class CookUpdateForm(UserChangeForm):
    years_of_experience = forms.IntegerField(min_value=0, max_value=80, label="Years of experience")

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = ["username", "years_of_experience", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields["password"]


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
