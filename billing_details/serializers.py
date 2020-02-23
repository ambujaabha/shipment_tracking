from .models import Billing_details
from rest_framework import serializers
from address.serializers import BillingAddressSerializer
import code
class BillingDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Billing_details
        fields = '__all__'

class ListBillingDetailsSerializer(serializers.ModelSerializer):

    address = BillingAddressSerializer()
    class Meta:
        model = Billing_details
        fields = '__all__'

class ShipmentBillingSerializer(serializers.ModelSerializer):
    address = BillingAddressSerializer()
    class Meta:
        model = Billing_details
        fields = '__all__'
    