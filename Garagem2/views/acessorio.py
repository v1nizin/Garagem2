from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem2.models import Acessorio
from Garagem2.serializers import AcessorioSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer