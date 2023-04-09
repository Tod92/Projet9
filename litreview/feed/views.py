from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator

from feed.models import Ticket, Review, Photo
from feed.forms import TicketForm, ReviewForm, PhotoForm, FollowUsersForm, TicketPicForm, AvatarPicForm

from authentication.models import UserFollows, User

from itertools import chain


@login_required
def follow_users(request):
    form = FollowUsersForm()
    following = UserFollows.objects.filter(
        user=request.user
    )
    followers = UserFollows.objects.filter(
        followed_user=request.user
    )
    if request.method == 'POST':
        form = FollowUsersForm(request.POST)
        if form.is_valid():
            searched_name = form.cleaned_data['rechercher_un_utilisateur']
            if searched_name != request.user.username:
                try :
                    aimed_user = User.objects.get(
                            username=searched_name
                    )
                    instance = UserFollows.objects.create(
                        user = request.user,
                        followed_user = aimed_user
                    )
                    instance.save()
                except:
                    messages.warning(request, 'Utilisateur non trouvé')
            else:
                messages.warning(request, 'Vous ne pouvez pas vous suivre vous-même')
    context = {
        'form': form,
        'following' : following,
        'followers' : followers
        }
    return render(request,
                  'feed/follow_users.html',
                  context
                  )

@login_required
def follow_delete(request, follow_id=None):
    follow = UserFollows.objects.get(id=follow_id)
    if follow.user == request.user:
        follow.delete()
    return redirect('follow-users')

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
    paginator = Paginator(tickets_and_reviews,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj' : page_obj
    }

    return render(request,
                  'feed/feed.html',
                  context=context
                  )
@login_required
def my_posts(request):
    """

    """
    # Construction de la liste à envoyer en context via querrys
    tickets = Ticket.objects.filter(
        user=request.user
    )
    reviews = Review.objects.filter(
        user=request.user
    )
    tickets_and_reviews = sorted(
        chain(tickets, reviews),
        key= lambda instance: instance.time_created,
        reverse= True
    )
    return render(request,
                  'feed/my_posts.html',
                  {'flux' : tickets_and_reviews}
                  )


@login_required
def ticket_detail(request, ticket_id=None):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request,
                  'feed/ticket_detail.html',
                  {'ticket' : ticket}
                  )


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
                  context
                  )


@login_required
def ticket_update(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if ticket.user != request.user:
        return redirect('feed')
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, instance=ticket)
        photo_form = TicketPicForm(request.POST, request.FILES, instance=ticket.photo)
        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.user = request.user
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user

            ticket.update_photo(photo)
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
    if ticket.user != request.user:
        return redirect('feed')
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')

    return render(request,
                  'feed/ticket_delete.html',
                  {'ticket' : ticket}
                  )


@login_required
def review_detail(request, review_id=None):
    review = Review.objects.get(id=review_id)
    return render(request,
                  'feed/review_detail.html',
                  {'review' : review}
                  )


@login_required
def review_create(request):
    """
    Page de création d'une critique en réponse au ticket selectionné, création
    de ticket imposée si ticket_id=None. Titre, note et commentaire.
    """
    if request.method == 'POST':
    # créer une instance de notre formulaire et le remplir avec les données POST
        form = ReviewForm(request.POST)
        ticket_form = TicketForm(request.POST)
        photo_form = TicketPicForm(request.POST, request.FILES)

        if all([form.is_valid(), ticket_form.is_valid()]):
            photo = None
            # Décalage de la condition pour que la photo ne soit pas obligatoire
            if photo_form.is_valid():
                photo = photo_form.save(commit=False)
                photo.user = request.user
                photo.save()
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.photo = photo
            ticket.save()
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('review',review.id)
    else:
        form = ReviewForm()
        ticket_form = TicketForm()
        photo_form = TicketPicForm()
    context = {
        'form' : form,
        'photo_form' : photo_form,
        'ticket_form' : ticket_form
    }
    return render(request,
                  'feed/review_create.html',
                  context)


@login_required
def review_update(request, review_id):
    review = Review.objects.get(id=review_id)
    if review.user != request.user:
        return redirect('feed')
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
                  {'form' : form}
                  )


@login_required
def review_delete(request, review_id=None):
    review = Review.objects.get(id=review_id)
    if review.user != request.user:
        return redirect('feed')
    if request.method == 'POST':
        review.delete()
        return redirect('feed')

    return render(request,
                  'feed/review_delete.html',
                  {'review' : review}
                  )
