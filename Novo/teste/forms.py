# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from http.server import DEFAULT_ERROR_MESSAGE

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password' ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','required':'true','maxlength': 255, 'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','required':'true','maxlength': 255,'placeholder': 'Último nome'}),
            'email': forms.EmailInput(attrs={'class':'form-control','required':'true','placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class':'form-control','maxlength': 255,'required':'true','placeholder': 'Nome de usuário'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','maxlength': 20,'required':'true','placeholder': 'Password'}),
            }
        DEFAULT_ERROR_MESSAGE = {
            'first_name':{
                    'required': 'Este campo é obrigatório'
                },
            'last_name':{
                    'required': 'Este campo é obrigatório'
                },
            'email':{
                    'required': 'Digite um campo valido'
                },
            'username':{
                    'required': 'Este campo é obrigatório'
                },
            'password':{
                    'required': 'Este campo é obrigatório'
                },
            
            }
        error_messages = {
            'first_name':{
                    'required': 'Este campo é obrigatório'
                },
            'last_name':{
                    'required': 'Este campo é obrigatório'
                },
            'email':{
                    'required': 'Digite um campo valido'
                },
            'username':{
                    'required': 'Este campo é obrigatório'
                },
            'password':{
                    'required': 'Este campo é obrigatório'
                },
            
            }
            
    def save(self,commit=True):
        user = super(UserModelForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:  
            user.save()
        return
    
            