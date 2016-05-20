from django import forms
from .models import Tint

class TintForm(forms.ModelForm):

    class Meta:
        model = Tint
        fields = ('hex_name', 'image')
            
class VoteForm(forms.Form):
    # winner_pk = forms.CharField(widget = forms.TextInput(attrs = {'vote_pk' : 'winner_pk'}))
    # loser_pk = forms.CharField(widget = forms.TextInput(attrs = {'vote_pk' : 'loser_pk'}))
    winner_pk = forms.CharField(max_length=10)
    loser_pk = forms.CharField(max_length=10)