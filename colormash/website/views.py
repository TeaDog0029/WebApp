from django.shortcuts import render, redirect, get_object_or_404
from .models import Tint
from .algorithm import convert_hex_to_rgb
from .forms import TintForm

# Create your views here.
def welcome_view(request):
    random_tints = Tint.objects.order_by('?')[:2]
    random_tint_one = random_tints[0]
    random_tint_two = random_tints[1]
    return render(request, 'website/base.html',{'random_tint_one': random_tint_one , 'random_tint_two': random_tint_two})

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


