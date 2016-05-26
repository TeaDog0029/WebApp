from django.contrib.auth.models import User, Group
from rest_framework import serializers

class TweetSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tweet
		fields = ('identifier','text','category')