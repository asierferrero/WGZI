from django import forms
from .models import Ikasle, Notak, Ikasgaiak

class IkasleForm(forms.ModelForm):
    class Meta:
        model = Ikasle
        fields = ['izena', 'abizena']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Notak
        fields = ['nota', 'ikasgai', 'ikasle']
        
class IkasgaiaForm(forms.ModelForm):
    class Meta:
        model = Ikasgaiak
        fields = ['izena', 'maila', 'hizkuntza']
