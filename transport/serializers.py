from .models import Transport
from rest_framework import serializers
class TransportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transport
        fields = ['transportId', 'transporterCode', 'trackAndTrace', 'shippingLabelId', 'shippingLabelCode']

class ShipmentTransportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transport
        fields = ['transportId', 'transporterCode', 'trackAndTrace', 'shippingLabelId', 'shippingLabelCode']