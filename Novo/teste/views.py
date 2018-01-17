from django.shortcuts import render
from django.http.response import HttpResponse
from teste.models import Usuario

# Create your views here.

def artigo(request, ano):
    return HttpResponse('Ola mundo. Esse e o ano de: '+ ano)

def home(request):
        usuarios = list(Usuario.objects.all())
        context = {
        'title':'List',
        'usuarios': usuarios
        }
        return render(request, 'template1/index.html', context)