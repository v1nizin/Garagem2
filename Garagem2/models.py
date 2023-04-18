from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome.upper()

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return  self.descricao
    
class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name = "Acessório"

class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = "Cores"

class Veiculo(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.cor} {self.ano}"
    
    class Meta:
        verbose_name = "Veículo"