from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem2.models import Categoria
from Garagem2.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer