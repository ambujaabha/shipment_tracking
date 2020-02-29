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
                "customerDetails": self.get_details(shipment, "customer"),
                "billingDetails": self.get_details(shipment, "billing_details")
            })
        return Response({"shipments": shipments})

    def get_details(self, class_obj, attr):
        return {
                    "salutationCode": getattr(class_obj, attr).salutationCode,
                    "firstName": getattr(class_obj, attr).firstName,
                    "surname": getattr(class_obj, attr).surname,
                    "streetName": getattr(class_obj, attr).address.streetName,
                    "houseNumber": getattr(class_obj, attr).address.houseNumber,
                    "houseNumberExtended": getattr(class_obj, attr).address.houseNumberExtended,
                    "addressSupplement": getattr(class_obj, attr).address.addressSupplement,
                    "extraAddressInformation": getattr(class_obj, attr).address.extraAddressInformation,
                    "zipCode": getattr(class_obj, attr).address.zipCode,
                    "city": getattr(class_obj, attr).address.city,
                    "countryCode": getattr(class_obj, attr).address.countryCode,
                    "email": getattr(class_obj, attr).email,
                    "company": getattr(class_obj, attr).company,
                    "vatNumber": getattr(class_obj, attr).vatNumber,
                    "chamberOfCommerceNumber": getattr(class_obj, attr).chamberOfCommerceNumber,
                    "orderReference": getattr(class_obj, attr).orderReference,
                    "deliveryPhoneNumber": getattr(class_obj, attr).deliveryPhoneNumber
                }

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

