from .models import Address
from rest_framework import serializers
class ShipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shipment
        fields = ['shipmentid', 'shipmentDate', 'shipmentReference', 'shipmentItems', 'transport', 'customer', 'billing_details']
    