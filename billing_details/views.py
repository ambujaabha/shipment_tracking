from django.shortcuts import render
from .models import Billing_details
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import BillingDetailsSerializer, ListBillingDetailsSerializer
import code
from address.models import Address

# Create your views here.
class Billing_detailsListView(generics.ListAPIView):
    # code.interact(local=dict(globals(), **locals()))
    queryset = Billing_details.objects.all()
    serializer_class = ListBillingDetailsSerializer

class Billing_detailsCreateView(generics.CreateAPIView):
    queryset = Billing_details.objects.all()
    serializer_class = BillingDetailsSerializer

    def create(self, request, *args, **kwargs):
        super(Billing_detailsCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created order.",
                    "result": request.data}
        return Response(response)

class Billing_detailsUpdateView(generics.UpdateAPIView):

    queryset = Billing_details.objects.all()
    serializer_class = BillingDetailsSerializer

    def update(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(Billing_detailsUpdateView, self).update(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated order having id: " + str(request.data["id"]) + ".",
                    "result": request.data}
        return Response(response)

