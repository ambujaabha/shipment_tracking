from django.db import models
from django.conf import settings
from addresses.models import Address


# Create your models here.
class Customer(models.Model):
    salutationCode = models.CharField(max_length = 120, blank= True)
    firstName = models.CharField(max_length = 120, blank= True)
    surname =  models.CharField(max_length = 120, blank= True)
    # streetName =  models.CharField(max_length = 120, blank= True)
    # houseNumber =  models.CharField(max_length = 120, blank= True)
    # houseNumberExtended = models.CharField(max_length = 120, blank= True)
    # addressSupplement = models.CharField(max_length = 120, blank= True)
    # extraAddressInformation = models.CharField(max_length = 120, blank= True)
    # zipCode = models.IntegerField(max_length = 120, blank= True)
    # city = models.CharField(max_length = 120, blank= True)
    # countryCode = models.IntegerField(max_length = 120, blank= True)
    address = models.ForeignKey("Address", null = False)
    email = models.EmailField(max_length = 120, blank= True)
    company = models.CharField(max_length = 120, blank= True)
    vatNumber = models.CharField(max_length = 120, blank= True)
    chamberOfCommerceNumber = models.CharField(max_length = 120, blank= True)
    orderReference = models.CharField(max_length = 120, blank= True)
    deliveryPhoneNumber = models.CharField(max_length = 120, blank= True)

    def __str__(self):
        return self.salutationCode