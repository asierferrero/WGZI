from django.db import models
from django.utils import timezone

# Create your models here.
class Pertsona(models.Model):
    izena = models.CharField(max_length=100)
    abizena = models.CharField(max_length=100)
    emaila = models.EmailField()

    def __str__(self):
        return f"{self.izena} {self.abizena}"

class Kotxe(models.Model):
    marka = models.CharField(max_length=100)
    modeloa = models.CharField(max_length=100)
    matrikula = models.CharField(max_length=10, unique=True)
    egoera = models.CharField(max_length=20, choices=[('libre', 'Libre'), ('alokatuta', 'Alokatuta')], default='libre')

    def __str__(self):
        return f"{self.marka} {self.modeloa} - {self.matrikula}"

class Alokatzea(models.Model):
    kotxea = models.ForeignKey(Kotxe, on_delete=models.CASCADE)
    pertsona = models.ForeignKey(Pertsona, on_delete=models.CASCADE)
    hasiera_data = models.DateTimeField(default=timezone.now)
    amaiera_data = models.DateTimeField()

    def __str__(self):
        return f"{self.pertsona} alokatu du {self.kotxea} ({self.hasiera_data} - {self.amaiera_data})"
