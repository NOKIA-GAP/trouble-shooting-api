# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Estacion

class EstacionForm(ModelForm):
    class Meta:
        model = Estacion
        # fields = ('responsable', 'prioridad')
        fields = '__all__'
