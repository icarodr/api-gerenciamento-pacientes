from django.db import models
from historicos.models import Historicos
from stdimage import StdImageField

# Create your models here.

def imagem_historico(instance, filename):
    return '/'.join(['historico', str(instance.id_historico.id_historico), filename])

class ImagemHistorico(models.Model):
    id_imagem_historico = models.AutoField(primary_key=True)
    imagem = models.StdImageField(blank=True, null=True, upload_to=imagem_historico)
    id_historico = models.ForeignKey(Historicos, related_name='imagens', on_delete=models.CASCADE, blank=False, null=False)