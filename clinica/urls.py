from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from pacientes.api.viewsets import PacientesViewSet
from agendamentos.api.viewsets import AgendamentoViewSet
from historicos.api.viewsets import HistoricosViewSet
from imagens.api.viewsets import ImagensHistoricoViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'pacientes', PacientesViewSet)
router.register(r'agendamentos', AgendamentoViewSet)
router.register(r'historicos', HistoricosViewSet)
router.register(r'imagens_historicos', ImagensHistoricoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
