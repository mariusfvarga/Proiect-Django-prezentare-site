from django.shortcuts import render
from django.http import HttpResponse

from .models import Produs, Recenzie

# Create your views here.
def salut(request):
    return HttpResponse("Salut")

def lista_produse(request):
    produse = Produs.objects.all()
    if "pret_maxim" in request.GET:
        produse = produse.filter(pret__lt=int(request.GET["pret_maxim"]))
    if "search" in request.GET:
        produse = produse.filter(titlu__icontains=request.GET["search"])
    
    produse = produse.order_by("pret")
   
    produse_formatat = [
        f"<li>{produs.titlu} - {produs.pret} - {produs.stoc}</li>"
        for produs in produse
    ]
    
    response_string = "<body><ul>"
    response_string += "".join(produse_formatat)
    response_string += "</ul></body>"
    return HttpResponse(response_string)

def produs(request, id):
    try:
        produs = Produs.objects.get(id=id)
        recenzii = produs.recenzie_set.all()
        recenzii_str = [recenzie.titlu for recenzie in recenzii]
    except Produs.DoesNotExist:
        return HttpResponse("404")
    return HttpResponse(f"{produs} <br /> {recenzii_str}")
 