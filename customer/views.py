from django.shortcuts import render
from .models import Customer
from rest_framework import generics, status
from rest_framework.response import Response
from address.models import Address
from .serializers import CustomerSerializer, ListCustomerSerializer
import code


# Create your views here.
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = ListCustomerSerializer

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(CustomerCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created order.",
                    "result": request.data}
        return Response(response)

class CustomerUpdateView(generics.UpdateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def update(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(CustomerUpdateView, self).update(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated order having id: " + str(request.data["id"]) + ".",
                    "result": request.data}
        return Response(response)

