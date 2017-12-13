# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (FormView, RedirectView,
                                  CreateView, DetailView,
                                  UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginUserForm, SigninUserForm, PerfilForm
from django.contrib.auth.models import User
from .models import Perfil

class LoginUser(FormView):
    form_class = LoginUserForm
    template_name = 'users/login_user.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginUser, self).form_valid(form)
        else:
            return self.form_invalid(form)

class LogoutUser(RedirectView):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUser, self).get(request, *args, **kwargs)

class SigninUser(CreateView):
    form_class = SigninUserForm
    model = User
    template_name = 'users/signin_user.html'
    success_url = reverse_lazy('index')

class DetailPerfil(LoginRequiredMixin, DetailView):
    login_url = 'users:login_user'
    model = Perfil
    template_name = 'users/detail_perfil.html'

class UpdatePerfil(LoginRequiredMixin, UpdateView):
    login_url = 'users:login_user'
    model = Perfil
    form_class = PerfilForm
    template_name = 'users/update_perfil.html'
    success_url = reverse_lazy('users:detail_perfil')

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()
