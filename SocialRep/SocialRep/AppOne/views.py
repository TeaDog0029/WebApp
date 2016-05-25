from django.shortcuts import render,redirect
from .models import Tweet, Stock
from .ftse100_api import convert_timestamp, build_dataset, graph
from .twitter import queryTwitter

# Create your views here.
def liveFeed(request):
	result_yahoo = graph("VOD","1d")
	top_tweets = queryTwitter('Vodafone customer', 5)
	return render(request, 'AppOne/base.html',{top_tweets: 'top_tweets'});