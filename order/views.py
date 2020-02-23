
from django.shortcuts import render
from .models import Order
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import OrderSerializer
import code

# Create your views here.

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(OrderCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created order.",
                    "result": request.data}
        return Response(response)

class OrderUpdateView(generics.UpdateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        # code.interact(local=dict(globals(), **locals()))
        super(OrderUpdateView, self).update(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated order having id: " + str(request.data["id"]) + ".",
                    "result": request.data}
        return Response(response)

