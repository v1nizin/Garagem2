from django.db import models
from Garagem2.models import Cor, Acessorio, Modelo
from uploader.models import Image


class Veiculo(models.Model):
    capa = models.ManyToManyField(
        Image,
        related_name="+",
    )
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    acessorio = models.ManyToManyField(Acessorio, related_name="Veiculo")

    def __str__(self):
        return f"{self.modelo}-{self.ano}-{self.cor}"

    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"