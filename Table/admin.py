from django.contrib import admin
from .models import Stocktick

# Register your models here.


@admin.register(Stocktick)
class StocktickAdmin(admin.ModelAdmin):
    list_display = ['Plant', 'Godown', 'OurLot',
                    'InvNo', 'Cases', 'RowNo', 'Remarks', 'Status', 'Pcase']
