# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import (
ConceptoNpo,
ConceptoNi,
)
from users.models import Perfil

class ConceptoNpoForm(ModelForm):

    class Meta:
        model = ConceptoNpo
        fields = ('contenido',)

class ConceptoNiForm(ModelForm):

    class Meta:
        model = ConceptoNi
        fields = ('contenido',)
