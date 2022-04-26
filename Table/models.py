from django.db import models

# Create your models here.
class Stocktick(models.Model):
    plant = models.CharField(max_length=50)
    godown = models.IntegerField()
    our_lot = models.IntegerField()
    recd_date = models.DateField()
    types = models.CharField(max_length=10)
    garden = models.CharField(max_length=100)
    grade = models.CharField(max_length=50)
    inv_no = models.CharField(max_length=50)
    cases = models.IntegerField()
    kg = models.IntegerField()
    net_kg = models.FloatField()
    row_no = models.CharField(max_length=50)
    remarks = models.TextField(max_length=500)
    status = models.BooleanField(default=False)