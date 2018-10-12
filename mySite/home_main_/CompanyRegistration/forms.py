from django import forms
from .models import Company_Registration,City


class Companyregistration(forms.ModelForm):

	class Meta:
		model= Data
		fields = ('company','country','city','PGnumber','priceMini','priceMaxi')
