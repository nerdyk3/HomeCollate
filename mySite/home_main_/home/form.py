from django import forms
from CompanyRegistration.models import City


class dummyForm(forms.ModelForm):

	class Meta:
		model = City    
		fields = ('name', )