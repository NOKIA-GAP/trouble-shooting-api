# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Button, HTML
from .models import Perfil

class LoginUserForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)

class SigninUserForm(UserCreationForm):
    email = forms.EmailField(label='Dirección de correo electrónico')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellidos')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(SigninUserForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            ButtonHolder(
                HTML('<div class="g-recaptcha" data-sitekey="6LcnejAUAAAAADbW7wDx_4AHLeOduCgS2PS4pNTj"></div><br>'),
                Submit('Registrar', 'Registrar', css_class='btn-success')
                ))

    def save(self, commit=True):
        user = super(SigninUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_active = False
        if commit:
            user.save()
        return user

class PerfilForm(ModelForm):

    class Meta:
        model = Perfil
        fields = ['celular', 'empresa']
