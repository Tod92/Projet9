from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from feed.models import Ticket

from feed.forms import CreateTicketForm, TicketForm

# Create your views here.
def feed(request):
    """
    Page de flux avec les tickets et critiques fonction des abonnements de
    l'utilisateur, ainsi que ses propres tickets et critiques, le tout trié
    par ordre décroissant de date de création
    """
    tickets = Ticket.objects.all()
    return render(request,'feed/feed.html',{'tickets' : tickets})

def ticket_detail(request, ticket_id=None):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request,'feed/ticket_detail.html', {'ticket' : ticket})

def ticket_create(request):
    """
    Page de création d'un ticket (demande de critique) avec titre, description
    et image.
    """
    if request.method == 'POST':
    # créer une instance de notre formulaire et le remplir avec les données POST
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket',ticket.id)
    else:
        form = TicketForm()

    return render(request,
                  'feed/create_ticket.html',
                  {'form' : form})

def ticket_update(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket',ticket.id)
    else:
        form = TicketForm(instance=ticket)
    return render(request,
                  'feed/update_ticket.html',
                  {'form' : form})

def ticket_delete(request, ticket_id=None):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')

    return render(request,'feed/ticket_delete.html', {'ticket' : ticket})

def form_sent(request):
    pass
    return render(request, 'feed/formsent.html')

def critic_create(request, ticket_id=None):
    """
    Page de création d'une critique en réponse au ticket selectionné, création
    de ticket imposée si ticket_id=None. Titre, note et commentaire.
    """
    return HttpResponse("<h1>Critic creation here</h1>")

def my_posts(request):
    pass
    return HttpResponse("<h1>My posts</h1>")
