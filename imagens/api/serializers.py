from dataclasses import field
from rest_framework import serializers
from imagens.models import ImagemHistorico

class ImagensHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemHistorico
        fields = '__all__'