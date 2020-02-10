from django.db import models

# Create your models here.
class Shipment(models.Model):
    billing_profile     = models.ForeignKey(BillingProfile, null=True, blank=True)
    Shipment_id            = models.CharField(max_length=120, blank=True) # AB31DE3
    shipping_address    = models.ForeignKey(Address, related_name="shipping_address",null=True, blank=True)
    billing_address     = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True)
    shipping_address_final    = models.TextField(blank=True, null=True)
    billing_address_final     = models.TextField(blank=True, null=True)
    cart                = models.ForeignKey(Cart)
    status              = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total      = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total               = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active              = models.BooleanField(default=True)
    updated             = models.DateTimeField(auto_now=True)
    timestamp           = models.DateTimeField(auto_now_add=True)