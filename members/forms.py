from django import forms
from django.contrib.auth.forms import UserCreationForm
from polls.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

