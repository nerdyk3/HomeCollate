from django.db import models
from django.utils import timezone
# from djangoratings.fields import RatingField


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Company_Registration(models.Model):
    company = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    PGnumber = models.IntegerField(default=0)
    priceMini = models.IntegerField(default=0)
    priceMaxi = models.IntegerField(default=0)
    create_time = timezone.now()
    # rating = RatingField(range=5)
    company_logo = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.company
