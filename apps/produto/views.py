from django.shortcuts import render
from .models import ItemOrder
# Create your views here.

def produto(request):
    itens = ItemOrder.objects.all()
    return render(request, 'home.html',{"itens":itens})