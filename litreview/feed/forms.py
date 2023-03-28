from django import forms

from feed.models import Ticket

class CreateTicketForm(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=1000)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        # exclude = ('user','descrition')
