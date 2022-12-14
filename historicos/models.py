from django.db import models
from agendamentos.models import Agendamentos

# Create your models here.

class Historicos(models.Model):
    id_historico = models.AutoField(primary_key=True)
    data = models.DateTimeField(auto_now_add=True)
    aparecimentos_sintomas = models.CharField(max_length=500, blank=True, null=True)
    duracao_sintomas = models.CharField(max_length=100, blank=True, null=True)
    local_dor = models.CharField(max_length=100, blank=True, null=True)
    tipo_dor = models.CharField(max_length=100, blank=True, null=True)
    conclusao = models.TextField(blank=True, null=True)
    #relacionando com o id de agendamentos 
    id_agendamento = models.ForeignKey(Agendamentos, related_name='historicos', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'historicos'
        