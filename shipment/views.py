from django.shortcuts import render
from .models import Shipment
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import ShipmentSerializer
import code
# Create your views here.

class ShipmentListView(generics.ListAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

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

