from django.db import models
from django.utils import timezone
from CompanyRegistration.models import City , Company_Registration
from multiselectfield import MultiSelectField

# Create your models here.
class Property_Registration(models.Model):
    Amenities_list=(
        ('TABLE/CHAIR','TABLE/CHAIR'),
        ('TOILET','TOILET'),
        ('ALMIRAH','ALMIRAH'),
        ('TV','TV'),
        ('FRIDGE','FRIDGE'),
        ('WIFI','WIFI'),
        ('BED','BED'),
        ('POWER BACKUP','POWER BACKUP'),
        ('R/O WATER','R/O WATER'),
        ('GYSERS','GYSERS'),
        ('FURNISHED','FURNISHED'),
        ('LAUNDARY','LAUNDARY'),
        ('PARKING','PARKING'),
    )
    Gender_list=(
        ('Boys','Boys'),
        ('Girls','Girls'),
        )
    Review_list = (('Very Good','Very Good'),('Good','Good'),('Normal','Normal'),('Bad','Bad'),)
    Rating_list = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    Area = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    Company = models.ForeignKey(Company_Registration, on_delete=models.SET_NULL, null=True)
    Property_Name = models.CharField(max_length=200,help_text='Your PG Name')
    Near_College = models.CharField(max_length=200,help_text='Colleges with 10 Kms')
    Address = models.CharField(max_length=200,help_text='Complete Address')
    State = models.CharField(max_length=200)
    Pincode = models.IntegerField(max_length=6)
    Single_Price = models.IntegerField(max_length=8,null=True, blank=True)
    Double_Price = models.IntegerField(max_length=8,null=True, blank=True)
    Triple_Price = models.IntegerField(max_length=8,null=True, blank=True)
    Quad_Price = models.IntegerField(max_length=8,null=True, blank=True)
    Latitude = models.FloatField(null=True, blank=True)
    Longitude = models.FloatField(null=True, blank=True)
    Review =models.CharField(max_length=20, choices=Review_list)
    Rating =models.CharField(max_length=20, choices=Rating_list)
    Gender = models.CharField(max_length=255,choices=Gender_list)
    pg_url = models.CharField(max_length=1000)
    Amenities = MultiSelectField(choices=Amenities_list)

    def __str__(self):
        return self.Property_Name
#
# class PropertAmenities(models.Model):
#     Ame_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.Ame_name
