from django.db import models
from django.conf import settings
from address.models import Address
# Create your models here.
class Billing_details(models.Model):
    salutationCode = models.CharField(max_length = 120, blank= True)
    firstName = models.CharField(max_length = 120, blank= True)
    surname = models.CharField(max_length = 120, blank= True)
    address = models.ForeignKey('address.Address', on_delete=True, null = True)
    email = models.EmailField(max_length = 120, blank= True)
    company = models.CharField(max_length = 120, blank= True)
    vatNumber =  models.IntegerField(blank= True)
    chamberOfCommerceNumber = models.IntegerField(blank= True)
    orderReference = models.CharField(max_length = 120, blank= True)
    deliveryPhoneNumber = models.IntegerField(blank= True)

    def __str__(self):
        return self.salutationCode
