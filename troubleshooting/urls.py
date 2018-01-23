"""troubleshooting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
admin.site.site_header = 'Trouble Shooting'
from users import urls as users_urls
from actividades import urls as actividades_urls
from solicitudeshw import urls as solicitudeshw_urls
from estaciones import urls as estaciones_urls
from asignaciones import urls as asignaciones_urls
from notificaciones import urls as notificaciones_urls
from conceptos import urls as conceptos_urls
from incidentes import urls as incidentes_urls
from reportes import urls as reportes_urls
from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include(users_urls, namespace='users')),
    url(r'^actividades/', include(actividades_urls, namespace='actividades')),
    url(r'^solicitudeshw/', include(solicitudeshw_urls, namespace='solicitudeshw')),
    url(r'^estaciones/', include(estaciones_urls, namespace='estaciones')),
    url(r'^asignaciones/', include(asignaciones_urls, namespace='asignaciones')),
    url(r'^notificaciones/', include(notificaciones_urls, namespace='notificaciones')),
    url(r'^conceptos/', include(conceptos_urls, namespace='conceptos')),
    url(r'^incidentes/', include(incidentes_urls, namespace='incidentes')),
    url(r'^reportes/', include(reportes_urls, namespace='reportes')),
]
