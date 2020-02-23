from django.db import models

# Create your models here.
class Address(models.Model):
    streetName =  models.CharField(max_length = 120, blank= True)
    houseNumber =  models.CharField(max_length = 120, blank= True)
    houseNumberExtended = models.CharField(max_length = 120, blank= True)
    addressSupplement = models.CharField(max_length = 120, blank= True)
    extraAddressInformation = models.CharField(max_length = 120, blank= True)
    zipCode = models.IntegerField(blank= True)
    city = models.CharField(max_length = 120, blank= True)
    countryCode = models.IntegerField(blank= True)

    def __str__(self):
        return self.streetName