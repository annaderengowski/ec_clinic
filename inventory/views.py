from django.shortcuts import render
from .models import *
from .forms import *

def stock_list(request):
    remedies = RemedyInventory.objects.prefetch_related('herbs').all()
    simples = SimpleInventory.objects.all()

    return render(request, 'inventory/stock_list.html', {'simples': simples, 'remedies': remedies})

def add_donation(request):

    if request.method == 'POST':
        form = DonationForm(request.POST)

        if form.is_valid():
            print('form is valid')
        else:
            print('form is not valid')
    else:
        form = DonationForm()

    return render(request, 'inventory/add_donation.html', {'form': form})

def dispense(request):
    simples = [SimpleInventory.objects.get(id=2), SimpleInventory.objects.get(id=5)]
    remedies = [RemedyInventory.objects.get(id=1)]
    return render(request, 'inventory/dispense.html', {'simples': simples, 'remedies': remedies})
