from django.shortcuts import render, redirect, get_object_or_404
from .models import Tint
from .algorithm import convert_hex_to_rgb, extract_pk
from .forms import TintForm, VoteForm

# Create your views here.
def welcome_view(request):
    voteForm = VoteForm(request.POST or None, auto_id=False)
    if (voteForm.is_valid()):
        winner_pk = voteForm.cleaned_data['winner_pk']
        loser_pk = voteForm.cleaned_data['loser_pk']
        winner = Tint.objects.get_object_or_404(pk=extract_pk(1, winner_pk))
        loser = Tint.objects.get_object_or_404(pk=extract_pk(2, loser_pk))
        winner.elo = elo(winner.elo, loser.elo,1)[0]
        winner.number_of_clicks+=1
        loser.elo = elo(winner.elo, loser.elo,1)[1]
        winner.save()
        loser.save()
    random_tints = Tint.objects.order_by('?')[:2]
    random_tint_one = random_tints[0]
    random_tint_two = random_tints[1]
    return render(request, 'website/base.html',{'random_tint_one': random_tint_one , 'random_tint_two': random_tint_two, voteForm: 'voteForm'})

def add_tint(request):
    form = TintForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        tint = form.save(commit=False)
        tint.hex_name = form.cleaned_data['hex_name'].lower()
        tint.rgb_name = convert_hex_to_rgb(tint.hex_name)
        tint.elo = 1400
        tint.rank = 1
        tint.save()
        return redirect('details', pk = tint.pk)
    return  render(request,'website/add_tint.html', {'form': form})

def details(request, pk):
    tint = get_object_or_404(Tint, pk = pk)
    return render(request, 'website/details.html', {'tint': tint})

def tint_list(request):
    tints = Tint.objects.order_by('elo')
    return render(request, 'website/rankings.html',{'tints':tints})


