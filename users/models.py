# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import choices


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30)
    perfil_usuario = models.CharField(max_length=255, choices=choices.PERFIL_USUARIO_CHOICES, blank=True, null=True)
    par = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='par', blank=True, null=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255)
    celular = models.CharField(max_length=255, blank=True, null=True)
    empresa = models.CharField(max_length=255, choices=choices.EMPRESA_CHOICES, blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creado',)
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
        permissions = (('perm_gap_administrador', 'Permisos para GAP Administrador'),
                       ('perm_gap_visitante', 'Permisos para GAP Visitante'),
                       ('perm_ni_ingeniero', 'Permisos para NI Ingeniero'),
                       ('perm_ni_asignador', 'Permisos para NI Asignador'),
                       ('perm_npo_ingeniero', 'Permisos para NPO Ingeniero'),
                       ('perm_npo_asignador', 'Permisos para NPO Asignador'),
                       ('perm_fm_lider', 'Permisos para FM Lider'),
                       ('perm_fm_permisos', 'Permisos para FM Permisos'),
                       ('perm_fm_supervisor', 'Permisos para FM Supervisor'),
                       ('perm_gap_monitoreo', 'Permisos para GAP Monitoreo'),)

    # def __unicode__(self):
    #     return u'%s %s' % (self.nombre, self.apellido)

    def __str__(self):
        return self.user.get_full_name()

    def _get_full_name(self):
        return u'%s %s' % (self.nombre, self.apellido)
    full_name = property(_get_full_name)

    def save(self, *args, **kwargs):
        user = self.user
        if user.is_active and self.perfil_usuario:
            perfil_u = self.perfil_usuario
            perfil, new = Perfil.objects.get_or_create(user=self.user)
            group, new= Group.objects.get_or_create(name=perfil_u)
            permission = Permission.objects.get(name='Permisos para '+perfil_u)
            group.permissions.add(permission)
            user.groups.add(group)
            self.slug = slugify(self.user)
            super(Perfil, self).save(*args, **kwargs)
        else:
            self.slug = slugify(self.user)
            super(Perfil, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('users:detail_perfil', kwargs={'slug': self.slug})

    @receiver(post_save, sender=User)
    def create_perfil(sender, instance, created, **kwargs):
        if created:
            perfil, new = Perfil.objects.get_or_create(user=instance,
                                                       nombre=instance.first_name,
                                                       apellido=instance.last_name,
                                                       email=instance.email,
                                                       nombre_completo=instance.get_full_name(),
                                                       )

    @receiver(post_save, sender=User)
    def save_perfil(sender, instance, **kwargs):
        instance.perfil.save()
