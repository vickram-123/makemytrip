from django.db import models

# Create your models here.
class Flight_details(models.Model):
    Fname= models.CharField(max_length=20)
    Fdate = models.DateField()
    Ffare = models.FloatField()
    Fstart = models.CharField(max_length=20)
    Fend = models.CharField(max_length=20)

