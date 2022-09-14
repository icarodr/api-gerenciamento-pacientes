from rest_framework import serializers
from agendamentos.models import Agendamentos
from historicos.api.serializers import HistoricosSerializer


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'

class AgendamentosDetalhesSerializer(serializers.ModelSerializer):
    historicos = HistoricosSerializer(many=True, read_only=True)

    class Meta:
        model = Agendamentos
        fields = [
            'id_agendamento',
            'data_hora',
            'data_criacao',
            'cancelado',
            'obs',
            'tipo',
            'historicos'
        ]