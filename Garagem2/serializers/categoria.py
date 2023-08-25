from rest_framework.serializers import ModelSerializer

from Garagem2.models import  Categoria




class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"