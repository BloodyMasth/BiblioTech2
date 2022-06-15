from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Livre
from .formulaire import LivreForm, RawLivreForm


# Create your views here
def index(request):
    livres = Livre.objects.all()

    return render(request, "index.html", {'livres': livres})


def jolie_carousel(request):
    livres = None

    return render(request, "jolie.html", {'livres': livres})


def formulaire(request):
    form = LivreForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/addlivre/')
    else:
        form = LivreForm()
    return render(request, 'addlivre.html', {'form': form})


# def formulaire(request):
#    form = RawLivreForm()
#    context = {
#        "form" : form
#    }
#    return  render(request, 'addlivre.html', context)

def roman(request):
    romans = Livre.objects.all().filter(genre='Roman')

    return render(request, "roman.html", {'romans': romans})


def bande_dessine(request):
    bds = Livre.objects.all().filter(genre='BD')

    return render(request, "BDs.html", {'bds': bds})


def recherche(request):
    query = request.GET.get('query')
    if not query:
        livres = Livre.objects.all()
    else:
        livres = Livre.objects.filter(serie__icontains=query)
    if not livres.exists():
        livres = Livre.objects.filter(auteur__icontains=query)
    return render(request, 'search.html', {'livres': livres})
