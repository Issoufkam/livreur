import requests
from django.shortcuts import render
from .forms import RechercheUtilisateurForm, DebitUtilisateurForm
from django.http import HttpResponseRedirect

API_URL = 'https://httpbin.org/get'

def recherche_utilisateur(request):
    if request.method == 'POST':
        form = RechercheUtilisateurForm(request.POST)
        if form.is_valid():
            numero_utilisateur = form.cleaned_data['numero']
            utilisateur = get_utilisateur_by_numero_from_api(numero_utilisateur)
            
            if utilisateur:
                return render(request, 'resultat_utilisateur.html', {'utilisateur': utilisateur})
            else:
                error_message = 'Désolé, ce numéro n\'existe pas.'
                return render(request, 'recherche_utilisateur.html', {'form': form, 'error_message': error_message})
    else:
        form = RechercheUtilisateurForm()

    return render(request, 'recherche_utilisateur.html', {'form': form})

def get_utilisateur_by_numero_from_api(numero):
    api_url = f'{API_URL}?numero={numero}'
    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête à l'API : {e}")
            return None
    else:
        return None


import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import DebitUtilisateurForm
from datetime import datetime

def montantF(request):
    status_message = None

    if request.method == 'POST':
        form = DebitUtilisateurForm(request.POST)
        if form.is_valid():
            montant = form.cleaned_data['montant']
            numero_crediteur = form.cleaned_data['numero_crediteur']

            # Logique pour effectuer le débit ici
            # Vous pouvez utiliser les données du formulaire pour effectuer les opérations nécessaires

            # Exemple d'intégration avec une API de paiement (utilisation de requests)
            api_url = 'https://httpbin.org/get'
            api_key = 'votre_cle_api_secrete'

            payload = {
                'montant': montant,
                'numero_crediteur': numero_crediteur,
                'api_key': api_key,
            }

            response = requests.post(api_url, data=payload)

            if response.status_code == 200:
                # Le débit a réussi

                # Informations pour la page de reçu
                recu_data = {
                    'nom': 'Nom de l\'utilisateur',  # Remplacez par le nom réel
                    'prenom': 'Prénom de l\'utilisateur',  # Remplacez par le prénom réel
                    'numero': numero_crediteur,
                    'montant': montant,
                    'date_heure': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }

                # Rediriger l'utilisateur vers la page de reçu
                return redirect('recu_payment', recu_data=recu_data)
            else:
                # Le débit a échoué
                status_message = 'Échec de la transaction. Veuillez réessayer.'
        else:
            status_message = 'Formulaire invalide. Veuillez corriger les erreurs.'

    else:
        form = DebitUtilisateurForm()

    return render(request, 'montant_a_recharger.html', {'form': form, 'status_message': status_message})

def recu_payment(request, recu_data):
    return render(request, 'recu_payment.html', {'recu_data': recu_data})
