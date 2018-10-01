from django import forms
from CompanyRegistration.models import City,Company_Registration


class dummyForm(forms.ModelForm):

	class Meta:
		model = City    
		fields = ('name', )

class dummyForm2(forms.ModelForm):

	class Meta:
		model = Company_Registration    
		fields = ('company', )