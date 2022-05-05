from django.db import models

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

    def __str__(self):
        return str(self.OurLot)
