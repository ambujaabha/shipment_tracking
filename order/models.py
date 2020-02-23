from django.db import models
from django.conf import settings

class Order(models.Model):
# Create your models here.
    orderId = models.AutoField(primary_key=True, auto_created=True)
    orderItemId =  models.CharField(max_length = 120, blank= True)
    latestDeliveryDate = models.DateTimeField(max_length = 120, blank= True)
    orderDate = models.DateTimeField(auto_now_add=True, auto_now=False)
    ean = models.IntegerField(blank= True)
    title = models.CharField(max_length = 120, blank= True)
    quantity = models.IntegerField(blank= True)
    offerPrice = models.CharField(max_length = 120, blank= True)
    offerCondition =  models.CharField(max_length = 120, blank= True)
    offerReference = models.CharField(max_length = 120, blank= True)
    fulfilmentMethod=  models.CharField(max_length = 120, blank= True)

    def __str__(self):
        return self.orderId

    