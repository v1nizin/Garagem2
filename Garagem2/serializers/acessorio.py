from rest_framework.serializers import ModelSerializer

from Garagem2.models import Acessorio


class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"