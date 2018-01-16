from django.db import models

# Create your models here.
class Usuario(models.Model): 
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length = 11)
    email = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.nome
    
class Historico(models.Model):
    nome = models.CharField(max_length = 20)
    tipo = models.CharField(max_length = 12)
    usuario = models.ForeignKey(Usuario,on_delete=models.PROTECT)
    
    
    def __str__(self):
        return self.nome