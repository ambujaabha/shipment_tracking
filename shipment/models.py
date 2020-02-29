from django.db import models
from django.conf import settings
from billing_details.models import Billing_details
from address.models import Address
from order.models import Order
from customer.models  import Customer
from transport.models import Transport
from django_mysql.models import ListCharField
from .utils import unique_shipmentItems_generator
from django.db.models.signals import pre_save
# Create your models here.
class Shipment(models.Model):
    shipmentId = models.AutoField(max_length= 120, primary_key=True, auto_created=True)
    shipmentDate = models.DateTimeField(auto_now= True)
    shipmentReference = models.CharField(max_length= 120, blank= True,)
    # shipmentItems = ListCharField(
    #      base_field = models.ForeignKey('order.Order', on_delete=True, name='order'),
    #      max_length = 120
    #     )
    shipmentItems = models.ManyToManyField('order.Order')
    transport = models.ForeignKey('transport.Transport', on_delete=True)
    customer = models.ForeignKey('customer.Customer', on_delete=True)
    billing_details = models.ForeignKey('billing_details.Billing_details', on_delete=True)

    def __str__(self):
        return self.shipmentId

def pre_save_create_shipmentItems(sender, instance, *args, **kwargs):
    if not instance.shipmentItems:
        instance.shipmentItems = unique_shipmentItems_generator(instance)

pre_save.connect(pre_save_create_shipmentItems, sender=Shipment)

