# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import (
ComentarioNpo,
ComentarioNi,
)
from users.models import Perfil

class ComentarioNpoForm(ModelForm):

    class Meta:
        model = ComentarioNpo
        fields = ('contenido',)

class ComentarioNiForm(ModelForm):

    class Meta:
        model = ComentarioNi
        fields = ('contenido',)
