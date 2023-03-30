from django import forms

from feed.models import Ticket, Review

# class CreateTicketForm(forms.Form):
#     title = forms.CharField(max_length=30)
#     description = forms.CharField(max_length=1000)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # fields = '__all__'
        fields = ('title', 'description')
        # exclude = ('user','descrition')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('ticket','rating', 'headline')
        # exclude = ('user','descrition')
