from django.db import models
from django.conf import settings

# Create your models here.
class Transport(models.Model):
    transportId = models.AutoField(primary_key=True, auto_created=True)
    transporterCode =  models.CharField(max_length = 120, blank= True)
    trackAndTrace = models.CharField(max_length = 120, blank= True)
    shippingLabelId = models.CharField(max_length = 120, blank= True)
    shippingLabelCode = models.CharField(max_length = 120, blank= True)

    def __str__(self):
        return self.transportId