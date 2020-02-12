from django.db import models
from django.conf import settings
from billing_details.models import Billing_details
from order.models import Order
from customer_details.models  import Customer_details
from transport.models import Transport
# Create your models here.
class Shipment(models.Model):
    ShipmentId = models.CharField(max_length= 120, blank= True)
    ShipmentDate = models.DateField(auto_now= True)
    ShipmentReference = models.CharField(max_length= 120, blank= True)
    ShipmentItems = models.CharField(max_length = 120, blank= True)

    def __str__(self):
        return self.ShipmentId
        