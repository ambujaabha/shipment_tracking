from django.db import models
from django.conf import settings

class Order(models.Model):
# Create your models here.
    orderItemId =  models.CharField(max_length = 120, blank= True)
    orderId = models.CharField(max_length = 120, blank= True)
    latestDeliveryDate = models.DateTimeField(max_length = 120, blank= True)
    orderDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    ean = models.IntegerField(max_length = 120, blank= True)
    title = models.CharField(max_length = 120, blank= True)
    quantity = models.CharField(max_length = 120, blank= True)
    offerPrice = models.CharField(max_length = 120, blank= True)
    offerCondition =  models.CharField(max_length = 120, blank= True)
    offerReference = models.CharField(max_length = 120, blank= True)
    fulfilmentMethod=  models.CharField(max_length = 120, blank= True)

    def __str__(self):
        return self.orderId

    