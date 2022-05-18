from django.contrib import admin
from .models import Stocktick,TeaBag

# Register your models here.


@admin.register(Stocktick)
class StocktickAdmin(admin.ModelAdmin):
    list_display = ['id','Plant', 'Godown', 'OurLot',
                    'InvNo', 'Cases', 'RowNo', 'Remarks', 'Status', 'Pcase']

@admin.register(TeaBag)
class TeaBagAdmin(admin.ModelAdmin):
    list_display = ['id','OurLot','PacketId']