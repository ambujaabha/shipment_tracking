from .models import Address
from rest_framework import serializers
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'streetName', 'houseNumber', 'houseNumberExtended', 'addressSupplement', 'extraAddressInformation', 'city', 'zipCode', 'countryCode']
class BillingAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['streetName', 'houseNumber', 'houseNumberExtended', 'addressSupplement', 'extraAddressInformation', 'city', 'zipCode', 'countryCode']
        # exclude = ['url', 'id']

class CustomerAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['streetName', 'houseNumber', 'houseNumberExtended', 'addressSupplement', 'extraAddressInformation', 'city', 'zipCode', 'countryCode']
        # exclude = ['url', 'id']

    

