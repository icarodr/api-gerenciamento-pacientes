from django.db import models
from pacientes.models import Pacientes

# Create your models here.
class Agendamentos(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data_hora = models.DateTimeField(blank=False, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    cancelado = models.BooleanField(default=False)
    obs = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, related_name='agendamentos', blank=False, null=False)
    class Meta:
        managed = True
        db_table = 'agendamentos'
        unique_together = ('data_hora', 'id_paciente')