from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produs(models.Model):
    titlu = models.CharField(max_length=50) #unique=True - daca vrem sa nu avem dubluri la nume
    pret = models.FloatField(db_index = True)
    stoc = models.IntegerField(default=0)
    descriere = models.CharField(max_length=1024, null=True, blank=True, help_text="Introduceti o descriere" )
    imagine = models.FileField(null=True, blank=True)
    
class Favorit(models.Model):
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
       
    