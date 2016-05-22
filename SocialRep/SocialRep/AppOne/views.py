from django.shortcuts import render,redirect
from .models import Tweet, Stock

# Create your views here.
def liveFeed(request):
	return render(request, 'AppOne/base.html',{});