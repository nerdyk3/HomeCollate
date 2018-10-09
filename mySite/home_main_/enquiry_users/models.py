from django.db import models
from django.utils import timezone
from CompanyRegistration.models import City , Company_Registration
from multiselectfield import MultiSelectField

class enquiry_web(models.Model):
	enquiry_type_list=(
	        ('Private Room','Private Room'),
	        ('Shared Room','Shared Room'),
	        )
	enquiry_user = models.CharField(max_length=200)
	enquiry_email = models.EmailField(max_length=200)
	enquiry_number = models.IntegerField(max_length=200)
	enquiry_area = models.CharField(max_length=200)
	enquiry_budget = models.IntegerField(max_length=200)
	enquiry_type = models.CharField(max_length=20,choices=enquiry_type_list)
	enquiry_comment = models.TextField(max_length=500)

	def __str__(self):
		return self.enquiry_user