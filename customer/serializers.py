from .models import Customer
from rest_framework import serializers
from address.serializers import CustomerAddressSerializer
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['salutationCode', 'firstName', 'surname', 'address', 'email', 'company', 'vatNumber', 'chamberOfCommerceNumber', 'orderReference', 'deliveryPhoneNumber' ]
    
class ListCustomerSerializer(serializers.ModelSerializer):

    address = CustomerAddressSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

class ShipmentCustomerSerializer(serializers.ModelSerializer):

    address = CustomerAddressSerializer()
    class Meta:
        model = Customer
        fields = '__all__'