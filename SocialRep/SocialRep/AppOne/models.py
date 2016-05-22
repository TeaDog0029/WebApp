from django.db import models
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
	identifier = models.IntegerField(default = 0)
	author = models.CharField(max_length = 50)
	date = models.DateTimeField(auto_now = True, auto_now_add = False)
	# To make sure we catch VF_UK tweets
	hashtag = models.CharField(max_length = 30)
	# Can be 'positive' or 'negative'
	category = models.CharField(max_length = 10)

	def __init__(self):
		return self.identifier

class Stock(models.Model):
	label = models.CharField(max_length = 10)
	# Values are in pennies, for instance: 212.13 = £2.1212 per share
	high = models.DecimalField(max_digits = 5, decimal_places = 2)
	low = models.DecimalField(max_digits = 5, decimal_places = 2)
	volume = models.IntegerField(default = 0)
	average = models.DecimalField(max_digits = 5, decimal_places = 2)
	openning_value = models.DecimalField(max_digits = 5, decimal_places = 2)
	closing_value = models.DecimalField(max_digits = 5, decimal_places = 2)


	def __init__(self):
		return self.label
		
		