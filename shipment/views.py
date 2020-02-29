from django.shortcuts import render
from .models import Shipment
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ShipmentSerializer, ListShipmentSerializer, ShipmentCustomerSerializer
import code
# Create your views here.

class ShipmentListView(generics.ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ListShipmentSerializer

    def list(self, request, *args):
        shipments = []
        for shipment in Shipment.objects.all():
            items = []
            for order in shipment.shipmentItems.all():
                items.append({
                    "orderItemId": order.orderItemId,
                    "orderId": order.orderId,
                    "orderDate": order.orderDate,
                    "latestDeliveryDate": order.latestDeliveryDate,
                    "ean": order.ean,
                    "title": order.title,
                    "quantity": order.quantity,
                    "offerPrice": order.offerPrice,
                    "offerCondition": order.offerCondition,
                    "offerReference": order.offerReference,
                    "fulfilmentMethod": order.fulfilmentMethod,

                })
            shipments.append({
                "shipmentId": shipment.shipmentId,
                "shipmentDate": shipment.shipmentDate,
                "shipmentReference": shipment.shipmentReference,
                "shipmentItems": items,
                "transport": {
                    "transportId": shipment.transport.transportId,
                    "transporterCode": shipment.transport.transporterCode,
                    "trackAndTrace": shipment.transport.trackAndTrace,
                    "shippingLabelId": shipment.transport.shippingLabelId,
                    "shippingLabelCode": shipment.transport.shippingLabelCode
                    },
                "customerDetails": {
                    "salutationCode": shipment.customer.salutationCode,
                    "firstName": shipment.customer.firstName,
                    "surname": shipment.customer.surname,
                    "streetName": shipment.customer.address.streetName,
                    "houseNumber": shipment.customer.address.houseNumber,
                    "houseNumberExtended": shipment.customer.address.houseNumberExtended,
                    "addressSupplement": shipment.customer.address.addressSupplement,
                    "extraAddressInformation": shipment.customer.address.extraAddressInformation,
                    "zipCode": shipment.customer.address.zipCode,
                    "city": shipment.customer.address.city,
                    "countryCode": shipment.customer.address.countryCode,
                    "email": shipment.customer.email,
                    "company": shipment.customer.company,
                    "vatNumber": shipment.customer.vatNumber,
                    "chamberOfCommerceNumber": shipment.customer.chamberOfCommerceNumber,
                    "orderReference": shipment.customer.orderReference,
                    "deliveryPhoneNumber": shipment.customer.deliveryPhoneNumber
                },
                "billingDetails": {
                    "salutationCode": shipment.billing_details.salutationCode,
                    "firstName": shipment.billing_details.firstName,
                    "surname": shipment.billing_details.surname,
                    "streetName": shipment.billing_details.address.streetName,
                    "houseNumber": shipment.billing_details.address.houseNumber,
                    "houseNumberExtended": shipment.billing_details.address.houseNumberExtended,
                    "addressSupplement": shipment.billing_details.address.addressSupplement,
                    "extraAddressInformation": shipment.billing_details.address.extraAddressInformation,
                    "zipCode": shipment.billing_details.address.zipCode,
                    "city": shipment.billing_details.address.city,
                    "countryCode": shipment.billing_details.address.countryCode,
                    "email": shipment.billing_details.email,
                    "company": shipment.billing_details.company,
                    "vatNumber": shipment.billing_details.vatNumber,
                    "chamberOfCommerceNumber": shipment.billing_details.chamberOfCommerceNumber,
                    "orderReference": shipment.billing_details.orderReference,
                    "deliveryPhoneNumber": shipment.billing_details.deliveryPhoneNumber
                }
            })

        return Response({"shipments": shipments})

class ShipmentCreateView(generics.CreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    def create(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(ShipmentCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created shipment.",
                    "result": request.data}
        return Response(response)

class ShipmentUpdateView(generics.UpdateAPIView):

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

    def update(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(ShipmentUpdateView, self).update(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated shipment having id: " + str(request.data["id"]) + ".",
                    "result": request.data}
        return Response(response)

