from django.shortcuts import render

from  apps.produto.models import ItemOrder,Categorie


# Create your views here.

def core(request):
    itens = ItemOrder.objects.all()
    categoria = Categorie.objects.all()
    dados = {
        "itens":itens,
        "categorias":categoria,
    }
    return render (request , "home.html",dados)


def produtos(request):
    itens = ItemOrder.objects.all()
    return render (request , "produtos.html",{"itens":itens})



def details_produto(request, produto_id):
    produto_id = ItemOrder.objects.get(id=produto_id)
    dados = {
        "produto": produto_id
    }
    return render(request, "product.html", dados)





def details_categories(request, categorie_id):
    categoria_id = Categorie.objects.get(id=categorie_id)
    dados = {
        "categoria": categoria_id
    }
    return render(request, "categorias.html", dados)

