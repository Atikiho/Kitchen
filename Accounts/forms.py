from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from Accounts.models import Cook


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