# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from teste.models import Usuario
from django.template import loader
from teste.forms import UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def artigo(request, ano):
    return HttpResponse('Ola mundo. Esse e o ano de: '+ ano)

def home(request):
        t = loader.get_template('template1/index.html')
        usuarios = list(Usuario.objects.all())
        context = {
        'title':'List',
        'usuarios': usuarios
        }
        return HttpResponse(t.render(context, request))
def dashboard(request):
        t = loader.get_template('Template2/docs/index.html')
        context = {
        }
        return HttpResponse(t.render(context, request))

@login_required
def dashboard2(request):
        t = loader.get_template('Template2/production/index.html')
        username = request.user.username
        context = {
            'usuario' : username,
        }
        return HttpResponse(t.render(context, request))

@login_required
def cadastro(request):
        t = loader.get_template('Cadastro.html')
        form = UserModelForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                context = {'form':form,'message':'Usuário cadastrado com sucesso!'}
                return HttpResponse(t.render(context, request))
        context = {'form':form}
        return HttpResponse(t.render(context, request))
   
def do_login(request):
    if request.method == 'POST':
        user=authenticate(username=request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            return dashboard2(request)
    autent = request.user.is_authenticated
    if autent:
        return dashboard2(request)
    t = loader.get_template('Login.html')
    context = {
    }
    return HttpResponse(t.render(context, request))    

def do_logout(request):
    t = loader.get_template('template1/index.html')
    context = {
    }
    return HttpResponse(t.render(context, request))    