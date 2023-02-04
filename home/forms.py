from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from home.models import UserPassword


class RegistrationForm(UserCreationForm):
    # class to create new user
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email',)

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@company.com'
            })
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(label=_("Your Username"),
                             widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(
        label=_("Your Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
    )


class UpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = UserPassword
        fields = ['id', 'username', 'password', 'application_type', 'website_name', 'website_url', 'application_name',
                  'game_name', 'game_developer']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }),
            'application_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'application type',
                'readonly': 'readonly',
            }),
            'website_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'website name',
            }),
            'website_url': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'website url',
            }),
            'application_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'application name',
            }),
            'game_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'game name',
            }),
            'game_developer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'game developer',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        application_type = cleaned_data.get('application_type')
        application_name = cleaned_data.get('application_name')
        website_name = cleaned_data.get('website_name')
        website_url = cleaned_data.get('website_url')
        game_name = cleaned_data.get('game_name')

        if application_type == 'Website' and not website_name:
            raise ValidationError({'website_name': 'Website name is required.'})

        if application_type == 'Website' and not website_url:
            raise ValidationError({'website_url': 'Website url is required.'})

        if application_type == 'Desktop application' and not application_name:
            raise ValidationError({'application_name': 'Application name is required.'})

        if application_type == 'Game' and not game_name:
            raise ValidationError({'game_name': 'Game name is required.'})
