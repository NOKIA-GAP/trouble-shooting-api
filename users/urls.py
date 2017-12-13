from django.conf.urls import url
from .views import (
LoginUser,
LogoutUser,
SigninUser,
DetailPerfil,
UpdatePerfil,
)

app_name = 'users'
urlpatterns = [
    url(r'^login_user/$', LoginUser.as_view(), name='login_user'),
    url(r'^logout_user/$', LogoutUser.as_view(), name='logout_user'),
    url(r'^signin_user/$', SigninUser.as_view(), name='signin_user'),
    url(r'^detail_perfil/(?P<slug>[-\w]+)/$', DetailPerfil.as_view(), name='detail_perfil'),
    url(r'^update_perfil/(?P<slug>[-\w]+)/$', UpdatePerfil.as_view(), name='update_perfil'),
]
