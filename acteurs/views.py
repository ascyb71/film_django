from django.shortcuts import render

from acteurs.forms import GestionActeurs

# Create your views here.
def ajoutActeur(request):
        
        form=GestionActeurs()
        context={"form":form}
        return render(request,'ajoutActeur.html',context)