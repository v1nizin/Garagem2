from rest_framework.viewsets import ModelViewSet

from Garagem2.models import Categoria, Marca
from Garagem2.serializers import CategoriaSerializer, MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CategoriaSerializer(ModelViewSet):
    class Meta:
        model = Categoria
        fields = "__all__"