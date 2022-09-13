from rest_framework import viewsets
from historicos.api.serializers import HistoricosSerializer
from historicos.models import Historicos

class HistoricosViewSet(viewsets.ModelViewSet):
    queryset = Historicos.objects.all().order_by('data')
    serializer_class = HistoricosSerializer