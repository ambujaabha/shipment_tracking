from .models import Order
from rest_framework import serializers
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderItemId', 'orderId', 'latestDeliveryDate', 'orderDate', 'ean', 'title', 'quantity', 'offerPrice', 'offerCondition', 'offerReference', 'fulfilmentMethod' ]
    
class ShipmentOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['orderItemId', 'orderId', 'latestDeliveryDate', 'orderDate', 'ean', 'title', 'quantity', 'offerPrice', 'offerCondition', 'offerReference', 'fulfilmentMethod' ]
    