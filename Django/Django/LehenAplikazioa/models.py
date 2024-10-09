from django.db import models
from django.utils import timezone

# Create your models here.
class Ikasle(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)

    # Balio berdinak ez sartzeko balidazioa
    class Meta:
        unique_together = ('izena', 'abizena')
        
    def __str__(self):
        return f"{self.izena} {self.abizena}"
    
class Ikasgaiak(models.Model):
    ikasgai_kodea = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    maila = models.CharField(max_length=50)
    hizkuntza = models.CharField(max_length=50)
    
    # Balio berdinak ez sartzeko balidazioa
    class Meta:
        unique_together = ('izena', 'maila', 'hizkuntza')
        
    def __str__(self):
        return f"{self.izena}"
    
class Notak(models.Model):
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    ikasgai = models.ForeignKey(Ikasgaiak, on_delete=models.CASCADE)
    ikasle = models.ForeignKey(Ikasle, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.ikasle} ikaslea {self.ikasgai} ikasgaian {self.nota} nota dauka."

