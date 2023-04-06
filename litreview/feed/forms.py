from django import forms

from feed.models import Ticket, Review, Photo, TicketPic, AvatarPic


from django.contrib.auth import get_user_model

User = get_user_model()

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['following']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # fields = '__all__'
        fields = ('title', 'description')
        # exclude = ('user','descrition')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')

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
