from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q

from feed.models import Ticket, Review, Photo
from feed.forms import TicketForm, ReviewForm, PhotoForm, FollowUsersForm, TicketPicForm, AvatarPicForm

from itertools import chain


@login_required
def follow_users(request):
    form = FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('feed')
    return render(request, 'feed/follow_users.html', context={'form': form})


@login_required
def feed(request):
    """
    Page de flux avec les tickets et critiques fonction des abonnements de
    l'utilisateur, ainsi que ses propres tickets et critiques, le tout trié
    par ordre décroissant de date de création
    """
    # Construction de la liste à envoyer en context via querrys
    tickets = Ticket.objects.filter(
        Q(user__in=request.user.following.all()) | Q(user=request.user)
    )
    reviews = Review.objects.filter(
        Q(user__in=request.user.following.all()) | Q(user=request.user)
    )
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key= lambda instance: instance.time_created,
        reverse= True
    )
    return render(request,'feed/feed.html',{'flux' : tickets_and_reviews})


@login_required
def ticket_detail(request, ticket_id=None):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request,'feed/ticket_detail.html', {'ticket' : ticket})


@login_required
def ticket_create(request):
    """
    Page de création d'un ticket (demande de critique) avec titre, description
    et photo.
    """
    if request.method == 'POST':
    # créer une instance de notre formulaire et le remplir avec les données POST
        ticket_form = TicketForm(request.POST)
        photo_form = TicketPicForm(request.POST, request.FILES)
        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.user = request.user
            photo.save()
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.photo = photo
            ticket.save()
            return redirect('ticket',ticket.id)
    else:
        ticket_form = TicketForm()
        photo_form = TicketPicForm()
    context = {
    'ticket_form': ticket_form,
    'photo_form': photo_form
    }
    return render(request,
                  'feed/ticket_create.html',
                  context)


@login_required
def ticket_update(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, instance=ticket)
        photo_form = TicketPicForm(request.POST, request.FILES, instance=ticket.photo)
        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.user = request.user
            photo.save()
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.photo = photo
            ticket.save()
            return redirect('ticket',ticket.id)
    else:
        ticket_form = TicketForm(instance=ticket)
        photo_form = TicketPicForm(instance=ticket.photo)
    context = {
    'ticket_form': ticket_form,
    'photo_form': photo_form
    }
    return render(request,
                  'feed/ticket_update.html',
                  context)


@login_required
def ticket_delete(request, ticket_id=None):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')

    return render(request,'feed/ticket_delete.html', {'ticket' : ticket})


@login_required
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
            review = form.save(commit=False)
            review.user = request.user
            review.save()
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
            review = form.save(commit=False)
            review.user = request.user
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


@login_required
def photo_upload(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.user = request.user
            # now we can save
            photo.save()
            return redirect('feed')
    return render(request, 'feed/photo_upload.html', context={'form': form})

# à supprimer après validation upload photos uniquement pour avatar user et tickets
@login_required
def photo_feed(request):
    photos = Photo.objects.all()
    return render(request, 'feed/photo_feed.html', context={'photos': photos})
