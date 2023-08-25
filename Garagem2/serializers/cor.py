from rest_framework.serializers import ModelSerializer

from Garagem2.models import Cor

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"
