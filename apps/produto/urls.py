from django.urls import path
from . import views

urlpatterns = [
    		path('', views.core, name='ProdutoHome'),
            path('produtos', views.produtos, name='Produtoslista'),
            path('produtos/<int:produto_id>', views.details_produto, name="itens_detalhes"),
            
            path('categorias/<int:categorie_id>', views.details_categories, name="categorias_detalhes")
	    ]