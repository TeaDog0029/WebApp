from django import forms
from .models import Tint

class TintForm(forms.ModelForm):

	class Meta:
		model = Tint
		fields = ('hex_name', 'image')
			
				