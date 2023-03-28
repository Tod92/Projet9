from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feed(request):
    """
    Page de flux avec les tickets et critiques fonction des abonnements de
    l'utilisateur, ainsi que ses propres tickets et critiques, le tout trié
    par ordre décroissant de date de création
    """
    return HttpResponse("<h1>Hi Babe</h1>")

def create_ticket(request):
    """
    Page de création d'un ticket (demande de critique) avec titre, description
    et image.
    """
    return HttpResponse("<h1>Ticket creation here</h1>")

def create_critic(request, ticket_id=None):
    """
    Page de création d'une critique en réponse au ticket selectionné, création
    de ticket imposée si ticket_id=None. Titre, note et commentaire.
    """
    return HttpResponse("<h1>Critic creation here</h1>")
