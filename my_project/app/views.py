from django.shortcuts import render
from django.http import HttpResponse

from .models import Produs, Recenzie

# Create your views here.
def salut(request):
    return render(request, "index.html")
    return HttpResponse("Salut")

def lista_produse(request):
    produse = Produs.objects.all().select_related("producator").prefetch_related("recenzie_set") 
    if "pret_maxim" in request.GET:
        produse = produse.filter(pret__lt=int(request.GET["pret_maxim"]))
    if "search" in request.GET:
        produse = produse.filter(titlu__icontains=request.GET["search"])
    
    produse = produse.order_by("pret")
    
    return render(request, "produse.html", {"produse": produse})


def produs(request, id):
    try:
        produs = Produs.objects.get(id=id)
        recenzii = produs.recenzie_set.all()
        recenzii_str = [recenzie.titlu for recenzie in recenzii]
    except Produs.DoesNotExist:
        return HttpResponse("Page not found 404")
    return render(request, "produs.html", {"produs":produs})
    
 