from django.shortcuts import render

from acteurs.forms import GestionActeurs
from acteurs.models import Acteur

# Create your views here.
def ajoutActeur(request):
        
        form=GestionActeurs(request.POST or None)
        print(request.POST)

        if form.is_valid():
            nom=form.cleaned_data['nom']
            email=form.cleaned_data['email1']
            nouvel_acteur=Acteur(nom=nom,email=email)
            nouvel_acteur.save()
            form=GestionActeurs()

        context={"form":form}
        return render(request,'acteurs/ajoutActeur.html',context)


def editActeur(request,acteur_id):
        acteur=Acteur.objects.get(id=acteur_id)
        form=GestionActeurs(request.POST or None,
        initial={'nom':acteur.nom,'email1':acteur.email,'email2':acteur.email})
        if form.is_valid():
            acteur.nom=form.cleaned_data['nom']
            acteur.email=form.cleaned_data['email1']
            acteur.save()
            context={"form":form}
            return render(request,'acteurs/editActeur.html',context)
        
def deleteActeur(request, acteur_id):
    acteur = Acteur.objects.get(id=acteur_id)
    acteur.delete()
    return redirect('ajoutActeur')