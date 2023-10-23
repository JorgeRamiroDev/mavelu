from django.db import models

# Create your models here.
class ItemOrder(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField()
    

    def __str__(self):
        return self.nome_produto