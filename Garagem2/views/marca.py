from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem2.models import Marca
from Garagem2.serializers import (
    MarcaSerializer,
)


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer