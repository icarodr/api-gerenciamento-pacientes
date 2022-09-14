from rest_framework import viewsets
from pacientes.models import Pacientes
from pacientes.api.serializers import PacienteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from pacientes.api.serializers import PacientesDetalhesSerializer

class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class = PacienteSerializer

    # Aqui esta um exemplo de uma action e seu metodo de construção, uma action basicamente é uma função dentro da classe
    @action(detail=True, methods=['get'])
    def detalhes(self, request, pk=None, *args, **kwargs):
        queryset = Pacientes.objects.filter(pk=pk)
        self.serializer_class = PacientesDetalhesSerializer
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)