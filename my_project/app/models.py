from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produs(models.Model):
    titlu = models.CharField(max_length=50) #unique=True - daca vrem sa nu avem dubluri la nume
    pret = models.FloatField(db_index = True)
    stoc = models.IntegerField(default=0)
    descriere = models.CharField(max_length=1024, null=True, blank=True, help_text="Introduceti o descriere" )
    imagine = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.titlu}"

    @property
    def rating(self):
        rating = 0
        recenzii = self.recenzie_set.all() 
        for recenzie in recenzii:
            rating += recenzie.rating
        try:
            return rating // len(recenzii)
        except ZeroDivisionError:
            return 0
                


class Recenzie(models.Model):
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)    
    titlu = models.CharField(max_length=20)
    descriere = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Recenzie {self.produs}"
    
class Favorit(models.Model):
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.produs}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=15)
    adresa = models.CharField(max_length=100)
    localitate = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.user}"
    
           
    