from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import Produs, Recenzie
from .forms import ContactForm

# Create your views here.
def salut(request):
    produse = Produs.objects.all().select_related("producator").prefetch_related("recenzie_set").order_by("-created")[:9]
    return render(request, "index.html", {"produse": produse})
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

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subiect = form.cleaned_data["subiect"]
            mesaj = form.cleaned_data["mesaj"]
            email = form.cleaned_data["email"]
            send_mail(subiect, mesaj, from_email="mariusss_1985@yahoo.com", recipient_list=[email])
            return redirect("/")
    return render(request, "contact.html", {"form": form})
    
 