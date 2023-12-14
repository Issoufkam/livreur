from django import forms

class RechercheUtilisateurForm(forms.Form):
    numero = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'Entrez le numéro',
            'class': 'votre-classe-css-personnalise',
            'style': 'width: 300px; height: 30px; border-radius: 5px;'  # Ajoutez des styles CSS personnalisés ici
        })
    )

    def clean_numero(self):
        numero = self.cleaned_data['numero']

        # Vérifier si le numéro commence par "01", "05" ou "07" et a un maximum de 10 chiffres
        if not (numero.startswith('01') or numero.startswith('05') or numero.startswith('07')) or not (len(numero) <= 10):
            raise forms.ValidationError("Le numéro doit commencer par '01', '05' ou '07' et avoir un maximum de 10 chiffres.")
        
        return numero


class DebitUtilisateurForm(forms.Form):
    montant = forms.DecimalField(min_value=0, required=True)
    numero_crediteur = forms.CharField(max_length=10, required=True)
    
    def clean_numero(self):
        numero = self.cleaned_data['numero']
        # Vérifier si le numéro commence par "01", "05" ou "07" et a un maximum de 10 chiffres
        if not (numero.startswith('01') or numero.startswith('05') or numero.startswith('07')) or not (len(numero) <= 10):
            raise forms.ValidationError("Le numéro doit commencer par '01', '05' ou '07' et avoir un maximum de 10 chiffres.")
        
        return numero