from django.shortcuts import render,redirect
from .models import Tweet, Stock
from .ftse100_api import convert_timestamp, build_dataset, graph
from .twitter import queryTwitter
from .mood import mood, averageMood
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import TweetSerializer

# Create your views here.
def liveFeed(request):
	result_yahoo = graph("VOD","1d")
	top_tweets = queryTwitter('VodafoneUK', 5)
	average_mood = averageMood(top_tweets)
	return render(request, 'AppOne/base.html',{'top_tweets': top_tweets, 'average_mood': average_mood});

class TweetViewSet(viewsets.ModelViewSet):
	# API endpoint that allow tweets to be read ... and edited?
	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer