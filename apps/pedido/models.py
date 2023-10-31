from django.db import models
from django.contrib.auth.models import User
from apps.produto.models import ItemOrder

# Create your models here.

class Order(models.Model):
    cliente = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_envio = models.DateTimeField(null=True, blank=True)
    data_entrega = models.DateTimeField(null=True, blank=True)
    itens = models.ManyToManyField(ItemOrder)

    def __str__(self):
        return f'Pedido de {self.cliente}'
    
    def status(self):
        if self.status:
            return "Em andamento"
        else:
            return "Processado"
        

    