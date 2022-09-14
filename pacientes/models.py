from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Pacientes(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateTimeField(blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    num_endereco = models.IntegerField(blank=True, null=True)
    bairro_endereco = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=100, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    rg = models.CharField(max_length=100, blank=True, null=True)

    #Todos os tipos de Field estão na documentação do Django

    class Meta:
        managed = True
        db_table = 'pacientes'

    