# -*- coding: utf-8 -*-

from django.conf.urls import url
from teste import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^artigo/(?P<ano>[0-9]{4})/$', views.artigo),
    url(r'^$', views.home),
    url(r'^login$', views.do_login),
    url(r'^logout$', views.do_logout),
    url(r'^cadastro$', views.cadastro),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard2$', views.dashboard2),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

