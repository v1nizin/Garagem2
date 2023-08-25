from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem2.models import Veiculo
from Garagem2.serializers import (
    VeiculoDetailSerializer,
    VeiculoListSerializer,
    VeiculoSerializer,
)



class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = {
        "list": VeiculoListSerializer,
        "retrieve": VeiculoDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, VeiculoSerializer)