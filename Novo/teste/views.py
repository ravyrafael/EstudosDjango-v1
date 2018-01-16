from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from teste.models import Usuario

# Create your views here.

def artigo(request, ano):
    return HttpResponse('Ola mundo. Esse e o ano de: '+ ano)

def home(request):
    context = {
        "title":"List"
        }
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', context)