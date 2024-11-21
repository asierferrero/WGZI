from django import forms
from .models import Alokatzea

class AlokatzeaForm(forms.ModelForm):
    class Meta:
        model = Alokatzea
        fields = ['pertsona', 'amaiera_data']
        widgets = {
            'amaiera_data': forms.DateInput(attrs={'type': 'date'}),
        }
