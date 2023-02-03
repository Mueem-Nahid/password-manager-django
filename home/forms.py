from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
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
    # website_name = forms.CharField(required=False)
    # website_url = forms.CharField(required=False)
    # application_name = forms.CharField(required=False)
    # game_name = forms.CharField(required=False)
    # game_developer = forms.CharField(required=False)

    class Meta:
        model = UserPassword
        fields = ['username', 'password', 'application_type', 'website_name', 'website_url', 'application_name',
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
