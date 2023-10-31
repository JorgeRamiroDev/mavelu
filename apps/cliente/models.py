from django.db import models

class Configuracao(models.Model):
   

    def __str__(self):
        return self.nome_empresa
