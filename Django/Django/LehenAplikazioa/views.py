from django.shortcuts import render, redirect
from .models import Ikasle, Notak
from .forms import IkasleForm, NotaForm, IkasgaiaForm

# Create your views here.
def ikasle_list(request):
    ikasleZerrenda = Ikasle.objects.all()
    # ikasleZerrenda = Ikasle.objects.filter(izena='Eneko')
    # ikasleZerrenda=Ikasle.objects.filter(izena='Ane').order_by('jaiotze_data')
    # ikasleZerrenda=Ikasle.objects.filter(izena='Ane').order_by(‘-jaiotze_data’)
    return render(request, 'ikasle_list.html', {'ikasleak': ikasleZerrenda})

def gehitu_ikaslea(request):
    if request.method == 'POST':
        form = IkasleForm(request.POST)
        if form.is_valid:
            ikasle = form.save()
        ikasle.save()
        return redirect('zerrenda-default')
    else:
        form = IkasleForm()
        return render(request, 'gehitu_ikaslea.html', {'form': form})
    
def nota_sartu(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid:
            nota = form.save()
        nota.save()
        return redirect('zerrenda-default')
    else:
        form = NotaForm()
        return render(request, 'nota_sartu.html', {'form': form})
    
def nota_zerrenda(request):
    notenZerrenda = Notak.objects.all()
    form = NotaForm()
    return render(request, 'nota_zerrenda.html', {'form': form, 'notak': notenZerrenda})
    
def gehitu_ikasgaia(request):
    if request.method == 'POST':
        form = IkasgaiaForm(request.POST)
        if form.is_valid:
            ikasgaia = form.save()
        ikasgaia.save()
        return redirect('zerrenda-default')
    else:
        form = IkasgaiaForm()
        return render(request, 'ikasgaia_gehitu.html', {'form': form})

def ezabatu_ikaslea(request):
    if request.method == 'POST':
        form = IkasleForm(request.POST)
        if form.is_valid:
            ikasle = form.save()
        ikasle.save()
        return redirect('zerrenda-default')
    else:
        form = IkasleForm()
        return render(request, 'ezabatu_ikaslea.html', {'form': form})