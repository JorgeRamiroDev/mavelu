from django.contrib import admin
from .models import ItemOrder,Categorie,Fornecedor
# Register your models here.
@admin.register(ItemOrder)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ['nome_produto','preco']
    list_display_links = ['nome_produto']
class ItemOrderInline(admin.TabularInline):
    model = ItemOrder
    extra = 0

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nome_categorie',]
    inlines = [ItemOrderInline]

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome_fornecedor',]