from django.shortcuts import render
from .models import *

def stock_list(request):
    remedies = RemedyInventory.objects.prefetch_related('herbs').all()
    simples = SimpleInventory.objects.all()

    return render(request, 'inventory/stock_list.html', {'simples': simples, 'remedies': remedies})

def add_donation(request):

    return render(request, 'inventory/add_donation.html', {})
