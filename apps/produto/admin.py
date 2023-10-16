from django.contrib import admin
from .models import ItemOrder
# Register your models here.
@admin.register(ItemOrder)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ['nome_produto','preco']
    list_display_links = ['nome_produto']