#from __future__ import unicode_literals
#from django.db import models
from django.db import models
from django.utils import timezone
from algorithm import convert_hex_to_rgb

# Create your models here.
class Tint(models.Model):
    hex_name = models.CharField(max_length = 30)
    rgb_name = models.CharField(max_length = 30)
    rank = models.IntegerField(default = 999)
    elo = models.IntegerField(default = 1400)
    image = models.ImageField(null = True, blank = True, height_field = "height_field", width_field = "width_field")
    height_field = models.IntegerField(default = 0)
    width_field = models.IntegerField(default = 0)
    number_of_clicks = models.IntegerField(default = 0)

    def __str__(self):
        return self.hex_name