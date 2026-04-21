from django import forms

class GestionActeurs(forms.Form):
    nom=forms.CharField(label="votre nom",max_length=50,required=True)
    email1=forms.EmailField(label="votre email",max_length=50,required=True)
    email2=forms.EmailField(label=" retaper votre email",max_length=50,required=True)