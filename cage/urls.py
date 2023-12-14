from django.urls import path
from .views import recherche_utilisateur, montantF


urlpatterns = [
    path('recherche/', recherche_utilisateur, name='recherche_utilisateur'),
    path('montant/', montantF, name="montant")
]
