from django import forms

class GestionActeurs(forms.Form):
    nom = forms.CharField(label='Nom ',max_length=50,widget=forms.TextInput(attrs={'style': 'display: block; marginbottom: 10px;'}))
    email1 = forms.EmailField(label="Tapez votre email ",max_length=100,widget=forms.EmailInput(attrs={'style': 'display: block;margin-bottom: 10px;'}))
    email2 = forms.EmailField(label="ReTapez votre email ", max_length=100,widget=forms.EmailInput(attrs={'style': 'display: block; margin-bottom:10px;'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        email1 = cleaned_data.get("email1")
        email2 = cleaned_data.get("email2")
        if email1 and email1.endswith("gmail.com"):
                self.add_error('email1', 'Adresse gmail non acceptée')
        if email2 and email2.endswith("gmail.com"):
                self.add_error('email2', 'Adresse gmail non acceptée')
        if email1 and email2 and email1 != email2:
                raise forms.ValidationError("Les adresses e-mail doiventcorrespondre.")
        return cleaned_data