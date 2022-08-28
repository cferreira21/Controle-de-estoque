from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mercadoria as merc
from .forms import formMercadoria

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def mercadoria(request):
    #itens = merc.objects.all()
    itens =  merc.objects.raw('SELECT * FROM dashboard_Mercadoria')

    if request.method == 'POST':
        form = formMercadoria(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:mercadoria')
    else:
        form = formMercadoria()
    
    context = {
        'itens': itens,
        'form': form,
    }

    return render(request, 'dashboard/mercadoria.html', context)

def delete_mercadoria(request, pk):
    item = merc.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard:mercadoria')
    return render(request, 'dashboard/delete_mercadoria.html')

def update_mercadoria(request, pk):
    item = merc.objects.get(id=pk)
    if request.method == 'POST':
        form = formMercadoria(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard:mercadoria')
    else:
        form = formMercadoria(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/update_mercadoria.html', context)
