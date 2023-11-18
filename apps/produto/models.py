from django.db import models

# Create your models here.



class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_fornecedor



class Categorie(models.Model):
    nome_categorie = models.CharField(max_length=100)
  


    def __str__(self):
        return self.nome_categorie
    
class ItemOrder(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    descricao = models.TextField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorie,on_delete=models.DO_NOTHING)
    imagem = models.ImageField(upload_to="foto_perfil/")
    

    

    def __str__(self):
        return self.nome_produto
    

