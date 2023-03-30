from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from feed.models import Ticket, Review

from feed.forms import TicketForm, ReviewForm




# Create your views here.
@login_required
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

@login_required
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
                  'feed/ticket_create.html',
                  {'form' : form})

@login_required
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
                  'feed/ticket_update.html',
                  {'form' : form})

@login_required
def ticket_delete(request, ticket_id=None):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')

    return render(request,'feed/ticket_delete.html', {'ticket' : ticket})


def review_detail(request, review_id=None):
    review = Review.objects.get(id=review_id)
    return render(request,'feed/review_detail.html', {'review' : review})

@login_required
def review_create(request):
    """
    Page de création d'une critique en réponse au ticket selectionné, création
    de ticket imposée si ticket_id=None. Titre, note et commentaire.
    """
    if request.method == 'POST':
    # créer une instance de notre formulaire et le remplir avec les données POST
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('review',review.id)
    else:
        form = ReviewForm()

    return render(request,
                  'feed/review_create.html',
                  {'form' : form})
@login_required
def review_update(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('review',review.id)
    else:
        form = ReviewForm(instance=review)
    return render(request,
                  'feed/review_update.html',
                  {'form' : form})
@login_required
def review_delete(request, review_id=None):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('feed')

    return render(request,'feed/review_delete.html', {'review' : review})
