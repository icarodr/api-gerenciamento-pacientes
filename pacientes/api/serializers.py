from rest_framework import serializers
from pacientes.models import Pacientes

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'