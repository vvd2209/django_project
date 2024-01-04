from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from catalog.forms import StyleForMixin
from users.models import User


class UserRegisterForm(StyleForMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleForMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
        self.fields['email'].disabled = True
