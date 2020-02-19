from .models import Address
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import AddressSerializer
from django.shortcuts import render
import code
class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(AddressCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created address.",
                    "result": request.data}
        return Response(response)

class AddressUpdateView(generics.UpdateAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    def update(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(AddressUpdateView, self).update(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated address having id: " + str(request.data["id"]) + ".",
                    "result": request.data}
        return Response(response)