from django import forms

from feed.models import Ticket, Review, Photo

# class CreateTicketForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     description = forms.CharField(max_length=1000)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # fields = '__all__'
        fields = ('title', 'description', 'photo')
        # exclude = ('user','descrition')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('ticket','rating', 'headline', 'body')
        # exclude = ('user','descrition')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'caption')
