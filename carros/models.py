from django.db import models


# Create your models here.

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT,
                              related_name="marca_carro")  # Adicionando uma chave estrangeira com a tabela Marca.
    # Este campo carregará uma lista de marca
    ano = models.IntegerField()
    valor = models.FloatField()
    placa = models.CharField(max_length=10, blank=True, null=True)
    imagem = models.ImageField(upload_to="carros/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)   

    def __str__(self):
        return self.modelo
    

class CarroInventario(models.Model):
    contagem_carros = models.IntegerField()
    carros_valor = models.FloatField()
    criado_em  = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']


    def __str__(self):
        return f'{self.contagem_carros} - {self.carros_valor}'

