from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Stocktick(models.Model):
    Plant = models.CharField(max_length=50)
    Godown = models.CharField(max_length=50)
    OurLot = models.IntegerField()
    RecdDate = models.DateField()
    Type = models.CharField(max_length=10)
    Garden = models.CharField(max_length=100)
    Grade = models.CharField(max_length=50)
    InvNo = models.CharField(max_length=50)
    Cases = models.IntegerField()
    Kg = models.FloatField()
    NetKg = models.FloatField()
    RowNo = models.CharField(max_length=50)
    Remarks = models.TextField(max_length=500)
    Status = models.BooleanField(default=True)
    Pcase = models.IntegerField(default=0)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.OurLot)
