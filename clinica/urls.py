from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from pacientes.api.viewsets import PacientesViewSet
from agendamentos.api.viewsets import AgendamentoViewSet
from historicos.api.viewsets import HistoricosViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PacientesViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'historicos', HistoricosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]