from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Garagem2.models import Cor
from Garagem2.serializers import CorSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer