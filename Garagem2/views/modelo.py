from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem2.models import Modelo
from Garagem2.serializers import (
    ModeloSerializer,
)


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer