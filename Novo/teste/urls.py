from django.conf.urls import url
from teste import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^artigo/(?P<ano>[0-9]{4})/$', views.artigo),
    url(r'^$', views.home),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

