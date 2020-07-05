from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse(
        """
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """
    )

