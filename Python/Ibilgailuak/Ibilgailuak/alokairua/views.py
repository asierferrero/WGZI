from django.shortcuts import render, get_object_or_404
from .models import Kotxe, Pertsona, Alokatzea
from .forms import AlokatzeaForm  # Formularioa inportatu
from django.http import HttpResponseRedirect
from django.urls import reverse

def kotxe_zerrenda(request):
    kotxeak = Kotxe.objects.all()
    return render(request, 'alokairua/kotxe_zerrenda.html', {'kotxeak': kotxeak})

def kotxe_alokatu(request, kotxe_id):
    kotxe = get_object_or_404(Kotxe, id=kotxe_id)

    if request.method == 'POST':
        form = AlokatzeaForm(request.POST)  # Formularioa betetzen denean POST datuak hartzen ditugu
        if form.is_valid():  # Formularioa baliozkoa den egiaztatzen dugu
            alokatzea = form.save(commit=False)  # Oraindik ez dugu gordeko
            alokatzea.kotxea = kotxe  # Kotxea gehitzen dugu alokatzean
            alokatzea.save()  # Alokatzea gordetzen dugu
            
            # Kotxearen egoera eguneratu
            kotxe.egoera = 'alokatutako'
            kotxe.save()  # Kotxearen egoera 'alokatutako' bihurtzen da
            
            return HttpResponseRedirect(reverse('kotxe_zerrenda'))

    else:
        form = AlokatzeaForm()  # GET eskaeran formulario huts bat ematen dugu

    return render(request, 'alokairua/kotxe_alokatu.html', {'kotxe': kotxe, 'form': form})
