from django import forms
from .models import enquiry_web


class enquiry_web_form(forms.ModelForm):

	class Meta:
		model= enquiry_web
		fields = ('enquiry_user','enquiry_email','enquiry_number','enquiry_area','enquiry_budget','enquiry_type','enquiry_comment')