from django import forms

from feed.models import Ticket, Review, Photo, TicketPic, AvatarPic
from authentication.models import UserFollows

from django.contrib.auth import get_user_model

User = get_user_model()

class FollowUsersForm(forms.Form):
    rechercher_un_utilisateur = forms.CharField(max_length=30)



class TicketForm(forms.ModelForm):
    # Surcharge de l'init afin de retirer les labels et utiliser placeholders
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ""
        self.fields['description'].label = ""


    class Meta:
        model = Ticket
        fields = ('title', 'description')
        widgets = {
        'title': forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Titre'
            }),
        'description': forms.Textarea(attrs={
            'class': "form-control",
            'placeholder': 'Description'
            })
        }




class ReviewForm(forms.ModelForm):
    CHOICES = [('0', 0),
               ('1', 1),
               ('2', 2),
               ('3', 3),
               ('4', 4),
               ('5', 5)]
    # Problème de passage du Radioselect à l'horizontal :
    # rating = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    rating = forms.ChoiceField(choices=CHOICES)


    # Surcharge de l'init afin de retirer les labels et utiliser placeholders
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headline'].label = ""
        self.fields['body'].label = ""

    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
        widgets = {
        'headline': forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Titre de la critique'
            }),
        'body': forms.Textarea(attrs={
            'class': "form-control",
            'placeholder': 'Saisir votre critique ici'
            })
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

class TicketPicForm(PhotoForm):
    class Meta:
        model = TicketPic
        fields = ['image']

class AvatarPicForm(PhotoForm):
    class Meta:
        model = AvatarPic
        fields = ['image']

# class CreateTicketForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     description = forms.CharField(max_length=1000)
