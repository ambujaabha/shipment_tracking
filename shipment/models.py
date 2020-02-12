from django.db import models
from django.conf import settings
from billing_details.models import Billing_details
from order.models import Order
from customer_details.models  import Customer_details
from transport.models import Transport
from django_mysql.models import ListCharField
# Create your models here.
class Shipment(models.Model):
    shipmentId = models.BigIntegerField(max_length= 120, blank= True)
    shipmentDate = models.DateTimeField(auto_now= True)
    shipmentReference = models.CharField(max_length= 120, blank= True)
    shipmentItems = ListCharField(
         base_field = models.ForeignKey(max_length = 120, blank= True)
        )

    def __str__(self):
        return self.ShipmentId

