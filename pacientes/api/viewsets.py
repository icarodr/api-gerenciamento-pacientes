from rest_framework import viewsets
from pacientes.models import Pacientes
from pacientes.api.serializers import PacienteSerializer

class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacienteSerializer