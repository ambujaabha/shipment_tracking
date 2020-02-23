from django.shortcuts import render
from .models import Transport
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import TransportSerializer
import code

# Create your views here.

class TransportListView(generics.ListAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

class TransportCreateView(generics.CreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def create(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(TransportCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created order.",
                    "result": request.data}
        return Response(response)

class TransportUpdateView(generics.UpdateAPIView):

    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

    def update(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(TransportUpdateView, self).update(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated order having id: " + str(request.data["id"]) + ".",
                    "result": request.data}
        return Response(response)

