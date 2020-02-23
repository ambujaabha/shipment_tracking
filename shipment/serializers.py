from .models import Shipment
from rest_framework import serializers
from order.serializers import ShipmentOrderSerializer
from transport.serializers import ShipmentTransportSerializer
from customer.serializers import ShipmentCustomerSerializer
from billing_details.serializers import ShipmentBillingSerializer
class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['shipmentId', 'shipmentDate', 'shipmentReference', 'shipmentItems', 'transport', 'customer', 'billing_details']
    
class ListShipmentSerializer(serializers.ModelSerializer):


    shipmentItems = ShipmentOrderSerializer()
    transport = ShipmentTransportSerializer()
    customer = ShipmentCustomerSerializer()
    billing_details = ShipmentBillingSerializer()
    class Meta:
        model = Shipment
        fields = '__all__'

# class ListTransportSerializer(serializers.ModelSerializer):
#     transport = ShipmentTransportSerializer()
#     class Meta:
#         model = Shipment
#         fields = '__all__'


# class ListCustomerSerializer(serializers.HyperlinkedModelSerializer):
#     customer = ShipmentCustomerSerializer()
#     class Meta:
#         model = Shipment
#         fields = '__all__'

# class ListBillingSerializer(serializers.HyperlinkedModelSerializer):

#     billing_details = ShipmentBillingSerializer()
#     class Meta:
#         model = Shipment
#         fields = '__all__'